from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<int:id>', views.pokemon, name='pokemon'),
    path('team/', views.team, name="team"),
    path('save_team/', views.save_team, name="save_team")
]
