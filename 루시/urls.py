from django.urls import path

from 루시 import views

app_name = '루시'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list')
]