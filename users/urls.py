from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.forms import LoginCustomForm
from users.views import LoginRequiredTemplateView, RegisterView, RegisterMessageView, UserPasswordRecoveryView, \
    UserPasswordSentView, ProfileView, confirm_register, UserUpdateView, UserListView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', form_class=LoginCustomForm), name='login'),
    path('login_required/', LoginRequiredTemplateView.as_view(), name='login_required'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/confirm/<str:code>/', confirm_register, name='confirm_register'),
    path('register/message/', RegisterMessageView.as_view(), name='register_message'),
    path('password_reset/', UserPasswordRecoveryView.as_view(), name='password_reset'),
    path('user_password_sent', UserPasswordSentView.as_view(), name='user_password_sent'),
    path('profile', ProfileView.as_view(), name='profile'),
    # path("users_list/", get_users_list, name='users_list'),
    path('users_list/', UserListView.as_view(), name='users_list'),
    path('edit/<int:pk>', UserUpdateView.as_view(), name='user_edit')
]
