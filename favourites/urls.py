from django.urls import path
from . import views

urlpatterns = [
    path(
        'favourites/',
        views.FavouritesList.as_view(),
        name='favourites-list'
    ),
    path(
        'favourites/<int:pk>/',
        views.FavouritesDetail.as_view(),
        name='favourites-detail'
    ),
]
