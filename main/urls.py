from django.urls import path

from main.apps import MainConfig
from main.views import MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, ClientListView, \
    ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete')
]
