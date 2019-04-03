from teams.models import Team, State
from users.models import Coach, Player
from tournaments.models import Tournament, Day, Game, Venue, Point, Foul, Win
from django.utils import timezone
from django.contrib.auth.models import User
State.objects.all().delete()
Team.objects.all().delete()
Coach.objects.all().delete()
Day.objects.all().delete()
Venue.objects.all().delete()
Tournament.objects.all().delete()
Game.objects.all().delete()
User.objects.exclude(username="admin").delete()
Win.objects.all().delete()


s = State(1, "Prueba", "PRB")
s.save()
t1 = Team(1, state=s, address="addprueba1", name="teamprueba1")
t1.save()
t1.generate_code()
t2 = Team(2, state=s, address="addprueba2", name="teamprueba2")
t2.save()
t2.generate_code()
up1 = User.objects.create_user('p1', 'p1@mail', 'pass')
up2 = User.objects.create_user('p2', 'p2@mail', 'pass')
uc1 = User.objects.create_user('c1', 'c1@mail', 'pass')
uc2 = User.objects.create_user('c2', 'c2@mail', 'pass')
c1 = Coach(1, user=uc1, telephone="1234567890", start_date=timezone.now(), team=t1)
c1.save()
c2 = Coach(1, user=uc2, telephone="1234567890", start_date=timezone.now(), team=t2)
c2.save()
p1 = Player(1, user=up1, date_of_birth=timezone.now(), telephone="12345667890", team=t1)
p1.save()
p2 = Player(2, user=up2, date_of_birth=timezone.now(), telephone="22345667890", team=t2)
p2.save()
tour = Tournament(1, name="tourprueba", start_date=timezone.now())
tour.save()
tour.team_set.add(t1)
tour.team_set.add(t2)
tour.save()
day = Day(1, number=1, is_inter_zone=False, start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=1), tournament=tour)
day.save()
place = Venue(1, name="venueprueba", courts=3, address="addressvenueprueba", state=s)
place.save()
g1 = Game(1, number=1, date_time=timezone.now(), team_local=t1, team_visitor=t2, court=1, day=day, venue=place)
g1.save()
g2 = Game(2, number=2, date_time=timezone.now()+timezone.timedelta(hours=2), team_local=t1, team_visitor=t2, court=2, day=day, venue=place)
g2.save()
(Point(1, game=g1, player=p1, value=1)).save()
(Point(2, game=g1, player=p2, value=2)).save()
(Foul(1, game=g1, player=p1, type='1')).save()
(Foul(2, game=g1, player=p2, type='1')).save()
g1.finish()
