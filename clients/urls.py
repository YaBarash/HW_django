from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientsCreateView, ClientsDetailView, ClientsListView, ClientsUpdateView, ClientsDeleteView, \
    EmailSettingsDeleteView, EmailSettingsCreateView, EmailSettingsListView, EmailSettingsUpdateView, HomePageView, \
    MailingMessageCreateView, MailingMessageListView, MailingMessageUpdateView, MailingMessageDeleteView, \
    MailLogListView, MailingClientListView, toggle_client

app_name = ClientsConfig.name

urlpatterns = [
    path('clients/home_page/', HomePageView.as_view(), name='main_page'),

    path('clients/create/', ClientsCreateView.as_view(), name='client_create'),
    path('clients/detail/<int:pk>/', ClientsDetailView.as_view(), name='client_detail'),
    path('clients/list/', ClientsListView.as_view(), name='client_list'),
    path('clients/update/<int:pk>/', ClientsUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientsDeleteView.as_view(), name='client_delete'),

    path('settings/create/', EmailSettingsCreateView.as_view(), name='emailsettings_create'),
    path('settings/list/', EmailSettingsListView.as_view(), name='emailsettings_list'),
    path('settings/update/<int:pk>/', EmailSettingsUpdateView.as_view(), name='emailsettings_update'),
    path('settings/delete/<int:pk>/', EmailSettingsDeleteView.as_view(), name='emailsettings_delete'),
    path('settings/edit/<int:pk>/', EmailSettingsUpdateView.edit_activate, name='emailsettings_edit'),

    path('message/create/', MailingMessageCreateView.as_view(), name='mailingmessage_create'),
    path('message/list/', MailingMessageListView.as_view(), name='mailingmessage_list'),
    path('message/update/<int:pk>/', MailingMessageUpdateView.as_view(), name='mailingmessage_update'),
    path('message/delete/<int:pk>/', MailingMessageDeleteView.as_view(), name='mailingmessage_delete'),

    path('mail_log/list/', MailLogListView.as_view(), name='maillog_list'),

    path('mailing_client/list/', MailingClientListView.as_view(), name='mailingclient_list'),
    path('settings/clients/<int:client_pk>', toggle_client, name='mailing_client_toggle'),


]