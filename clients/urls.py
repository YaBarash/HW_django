from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientsCreateView, ClientsDetailView, ClientsListView, ClientsUpdateView, ClientsDeleteView

app_name = ClientsConfig.name

urlpatterns = [
    path('create/', ClientsCreateView.as_view(), name='client_create'),
    path('detail/<int:pk>/', ClientsDetailView.as_view(), name='client_detail'),
    path('list/', ClientsListView.as_view(), name='client_list'),
    path('update/<int:pk>/', ClientsUpdateView.as_view(), name='client_update'),
    path('delete/<int:pk>/', ClientsDeleteView.as_view(), name='client_delete'),
]