from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientsCreateView, ClientsDetailView, ClientsListView, ClientsUpdateView, ClientsDeleteView, \
    EmailSettingsDeleteView, EmailSettingsCreateView, EmailSettingsListView, EmailSettingsUpdateView, HomePageView

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


]