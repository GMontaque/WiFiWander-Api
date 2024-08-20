from django.urls import path
from favourites import views

urlpatterns = [
    path('favourites/', views.FavouritesList.as_view()),
    path('favourites/<int:pk>/', views.FavouritesDetail.as_view()),
]
