from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Player
from tournaments.models import Tournament
from teams.models import Team
from users.models import Player, Coach
from django.shortcuts import redirect
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.views.decorators.csrf import csrf_protect


from .forms import PlayerForm,UserForm,LoginForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

from tournaments.models import Team


def get_team(user):
    if not user.is_authenticated:
        return ""
    try:
        model = Coach.objects.get(user=user)
    except ObjectDoesNotExist:
        model = Player.objects.get(user=user)
    return model.team


def init_context(context, tournament, team):
    context["day"] = tournament.get_current_day().number
    context["tournament"] = tournament.pk
    context["team"] = team.pk


def index(request):
    template = loader.get_template('../templates/header.html')
    players = Player.objects.all()
    context={"players":players,
    }

    return HttpResponse(template.render(context,request))


@login_required
def logged_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    return render(request,'logged_index.html',{'user':user})



def registerUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            user = authenticate(request, username=new_user.username, password=user_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/users/playerform.html')
    user_form = UserForm()
    return render(request, '../templates/userform.html', {'user_form': user_form})




def registerPlayer(request):
    if request.method == 'POST':
        player_form = PlayerForm(request.POST)
        if player_form.is_valid() and request.user.is_authenticated:
            code = player_form.cleaned_data.get("code")
            new_player = Player(
                user=request.user,
                team=Team.objects.get(code=code),
                date_of_birth=player_form.cleaned_data.get("date_of_birth"),
                telephone=player_form.cleaned_data.get("telephone"),
                sex=player_form.cleaned_data.get("sex")
            )
            new_player.save()
            return redirect('/users/login.html')
    else:
        player_form=PlayerForm()
    return render(request, '../templates/playerform.html', {'player_form': player_form})


def user_login(request):
    if request.method == 'POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_superuser:
                    return redirect('/admin/')
                pk = user.pk
                try:
                    model = Player.objects.get(user=pk)
                except Player.DoesNotExist:
                    model = Coach.objects.get(user_id=pk)
                team_id = model.team.id
                tournament_id = Tournament.objects.get(team_set=team_id, is_active=True).id
                if user.is_active:
                    login(request,user)
                    return redirect('/tournaments/'+str(tournament_id)+'/day/1')
                else:
                    return HttpResponse('Disabled account')

        else:
            return HttpResponse('Wrong credentials')
    else:
        login_form=LoginForm()
    return render(request,'../templates/login.html',{'login_form':login_form})


def logoutUser(request):
    logout(request)
    return redirect('/tournaments/')


def remove_player(request):
    if request.user.is_active:
        try:
            c = Coach.objects.get(user=request.user,
                                  team=Player.objects.get(id=int(request.GET.get("player"))).team)
        except Coach.DoesNotExist:
            return redirect("/tournaments/" + request.GET.get("tournament") + "/teams/" + request.GET.get("team"))
        p = Player.objects.get(id=request.GET.get("player"))
        p.user.delete()
        p.delete()
    return redirect("/tournaments/" + request.GET.get("tournament") + "/teams/" + request.GET.get("team"))
