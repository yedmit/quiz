from django.urls import path

from . import views

urlpatterns = [
    path('', views.polls_index, name='polls_index'),
]
