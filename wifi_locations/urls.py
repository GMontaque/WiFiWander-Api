from django.urls import path
from wifi_locations import views

urlpatterns = [
    path('wifi_locations/', views.LocationList.as_view(), name='wifi_location_list'),
    path('wifi_locations/<int:pk>/', views.Location.as_view(), name='wifi_location_detail'),
]
