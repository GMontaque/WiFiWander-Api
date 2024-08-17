from django.urls import path
from wifi_locations import views

urlpatterns = [
    path('wifi_locations/', views.LocationList.as_view()),
    path('wifi_locations/<int:pk>/', views.Location.as_view()),
    path('address/', views.AddressList.as_view()),
]
