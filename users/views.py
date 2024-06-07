import random
import string

from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, FormView, UpdateView, ListView

from config.settings import EMAIL_HOST_USER
from users.forms import RegisterForm, UserPasswordResetForm, UserProfileForm, UserManagerForm
from users.models import User


class RegisterMessageView(TemplateView):
    template_name = 'users/register_message.html'


class LoginRequiredTemplateView(TemplateView):
    template_name = 'users/login_required.html'


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_message')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        code = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        user.verification_code = code
        current_host = self.request.get_host()
        user.save()

        send_mail('Регистрация на сайте Sky-mailing',
                  f"""Подтвердите свой профиль, перейдя по ссылке\n 
                  http://{current_host}/users/register/confirm/{code}/""",
                  EMAIL_HOST_USER,
                  [user.email])
        return super().form_valid(form)


def confirm_register(request, code):
    user = get_object_or_404(User, verification_code=code)
    user.is_active = True
    user.save()
    return HttpResponseRedirect('/users/login')


class UserPasswordRecoveryView(FormView):
    form_class = UserPasswordResetForm
    template_name = 'users/user_password_reset.html'
    success_url = reverse_lazy('users:user_password_sent')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        characters = string.ascii_letters + string.digits
        new_password = ''.join(random.choice(characters) for _ in range(10))
        user.password = make_password(new_password)
        user.save()
        send_mail('Восстановление пароля на сайте Sky-mailing',
                  f'Ваш новый пароль: {new_password}', EMAIL_HOST_USER,
                  [user.email])
        return super().form_valid(form)


class UserPasswordSentView(TemplateView):
    template_name = 'users/user_password_sent.html'


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.set_is_active'
    extra_context = {'title': 'Список пользователей сервиса'}


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserManagerForm
    permission_required = 'users.set_is_active'
    success_url = 'users:users_list'

    def get_success_url(self):
        return reverse('users:users_list')
