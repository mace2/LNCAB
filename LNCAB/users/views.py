from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import  CreateView
from .forms import PlayerForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PlayerForm


def registerPlayer(request):
    if request.method == 'POST':
        player_form = PlayerForm(request.POST)
        if player_form.is_valid():
            new_player=player_form.save(commit=False)
            #new_player.set_password(player_form.cleaned_data['password'])
            new_player.save()
            return render(request,'../templates/playerform_done.html',{'new_player':new_player})
    else:
        player_form=PlayerForm()
    return render(request, '../templates/playerform.html', {'player_form': player_form})







def index(request):
    return HttpResponse("Hello, world. You're at the users index.")


