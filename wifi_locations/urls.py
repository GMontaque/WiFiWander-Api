from django.urls import path
from wifi_locations import views

urlpatterns = [
    path('wifi_location/', views.LocationList.as_view()),
    path('wifi_location/<int:pk>/', views.Location.as_view()),
    path('address/', views.AddressList.as_view()),
]
