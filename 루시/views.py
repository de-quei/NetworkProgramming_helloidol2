from django.shortcuts import render
from django.views.generic import ListView

from 루시.models import Character

class CharacterListView(ListView):
    model = Character
    # character_list = Character.objects.all() # DB에 model 내 데이터를 다 가져오자
    # return render(request, '루시/character_list.html', context={'character_list':character_list}) # model_list.html에 model_list라는 키로 DB에서 가져온 데이터를 넣어 render