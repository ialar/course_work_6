from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from main.forms import MailingForm, MessageForm, ClientForm
from main.models import Mailing, Message, Logs, Client


class MailingListView(ListView):
    model = Mailing
    extra_context = {'title': 'Список рассылок'}


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailing_list')
    extra_context = {'title': 'Создание рассылки'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form, *args, **kwargs):
        if form.is_valid():
            new_mailing = form.save(commit=False)
            new_mailing.owner = self.request.user
            new_mailing.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailing_list')
    extra_context = {'title': 'Редактирование рассылки'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailingDetailView(DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['clients'] = list(self.object.client.all())
        context_data['logs'] = list(Logs.objects.all())
        return context_data


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:mailing_list')


class MessageListView(ListView):
    model = Message
    extra_context = {'title': 'Список сообщений'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = Message.objects.filter(owner=self.request.user)
        return queryset


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:message_list')
    extra_context = {'title': 'Создание сообщения'}


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse('main:message_detail', args=[self.kwargs.get('pk')])


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('main:message_list')


class ClientListView(ListView):
    model = Client
    extra_context = {'title': 'Список клиентов'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = Client.objects.filter(owner=self.request.user)
        return queryset


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:client_list')
    extra_context = {'title': 'Добавить клиента'}

    def form_valid(self, form):
        new_client = form.save()
        new_client.owner = self.request.user
        new_client.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('main:client_list')
