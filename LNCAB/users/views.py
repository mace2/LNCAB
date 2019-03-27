from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import  CreateView
from .forms import PlayerForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Player

from .forms import PlayerForm,UserForm



def index(request):
    template = loader.get_template('../templates/header.html')
    players = Player.objects.all()
    context={"players":players,
    }

    return HttpResponse(template.render(context,request))



def reigsterUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            # new_player.set_password(player_form.cleaned_data['password'])
            new_user.save()
            return render(request, '../templates/playerform.html', {'new_user': new_user})
    else:
        user_form = UserForm()
    return render(request, '../templates/userform.html', {'user_form': user_form})




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








