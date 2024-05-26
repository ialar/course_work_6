from django.urls import path

from main.apps import MainConfig
from main.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
]
