from django.urls import path
from possibles import views

urlpatterns = [
    path('possibles/', views.PossiblesList.as_view()),
    path('possibles/<int:pk>/', views.PossiblesDetail.as_view()),
]
