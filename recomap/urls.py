from django.urls import path
from . import views

app_name = 'recomap'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('map/', views.MapView.as_view(), name='map'),
    path('marker/', views.MarkerReadListView.as_view(), name='marker_read_list'),
    path('marker/detail/<int:pk>/', views.MarkerReadDetailView.as_view(), name='marker_read_detail'),
    path('marker/delete/<int:pk>/', views.MarkerDeleteView.as_view(), name='marker_delete'),
    path('marker/update/<int:pk>/', views.MarkerUpdateView.as_view(), name='marker_update'),
    path('marker/create/', views.MarkerCreateView.as_view(), name='marker_create'),
]
