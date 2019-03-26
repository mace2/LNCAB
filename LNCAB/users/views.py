from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Player
from django.shortcuts import redirect

from .forms import PlayerForm,UserForm



def index(request):
    template = loader.get_template('../templates/header.html')
    players = Player.objects.all()
    context={"players":players,
    }

    return HttpResponse(template.render(context,request))



def registerUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            return redirect('/users/playerform.html')
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








