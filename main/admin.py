from django.contrib import admin

from main.models import Mailing, Message, Client


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'start_date', 'next_date', 'end_date', 'periodicity', 'message', 'owner', 'status', 'is_active'
    )
    list_filter = ('start_date',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'text', 'owner')


@admin.register(Client)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment', 'owner')
