from django.contrib import admin


@admin.register
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)


@admin.register
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('client', 'sent_at',)
    ordering = ('owner', ' letter_subject',)


@admin.register
class EmailSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'stop_time', 'status',)


@admin.register
class MailLogAdmin(admin.ModelAdmin):
    list_display = ('try_status', 'last_attempt',)
