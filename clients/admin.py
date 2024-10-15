from django.contrib import admin

from clients.models import MailLog, EmailSettings, MailingMessage, Client, MailingClient


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('owner', 'letter_subject',)


@admin.register(EmailSettings)
class EmailSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'stop_time', 'status',)


@admin.register(MailLog)
class MailLogAdmin(admin.ModelAdmin):
    list_display = ('try_status', 'last_attempt',)


@admin.register(MailingClient)
class MailingClientAdmin(admin.ModelAdmin):
    list_display = ('client', 'mailing',)
