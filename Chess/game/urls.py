from django.urls import path
from .views import game, move
urlpatterns = [
    path('', game, name='game'),
    path('move/', move, name='move'),
]