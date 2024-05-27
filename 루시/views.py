from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from 루시.models import Character

class CharacterListView(ListView):
    model = Character
    # character_list = Character.objects.all() # DB에 model 내 데이터를 다 가져오자
    # return render(request, '루시/character_list.html', context={'character_list':character_list}) # model_list.html에 model_list라는 키로 DB에서 가져온 데이터를 넣어 render

class CharacterDetailView(DetailView):
    model = Character
    # character = Character.objects.get(pk=pk)
    # return render(request, '루시/character_detail.html', context=('character': character)

class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'feature'] # '__all__'
    template_name_suffix = '_create' # character_form.html --> character_create.html
    success_url = reverse_lazy('루시:character_list') # 만들기 성공했을 때 이동할 URL