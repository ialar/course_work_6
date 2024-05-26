from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from main.models import Mailing, Client, Message, Logs


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
