from teams.models import Team, State
from users.models import Coach
from tournaments.models import Tournament, Day, Game, Venue
from django.utils import timezone


# s = State("Prueba", "PRB")
# s.save()

s = State.objects.get(code="PRB")
c1 = Coach("Pruebencio", "Pruebez Prueba", "1234567890", "prueba@prueba.com", timezone.now())
c1.save()
c2 = Coach("Pruebencio2", "Pruebez2 Prueba2", "1234567892", "prueba2@prueba2.com", timezone.now())
c2.save()
t1 = Team(c1, s, "addprueba1", "teamprueba1")
t1.save()
t2 = Team(c2, s, "addprueba2", "teamprueba2")
t2.save()
tour = Tournament("tourprueba", timezone.now())
tour.save()
tour.teams.add(t1)
tour.teams.add(t2)
tour.save()
day = Day(1, False, timezone.now(), timezone.now() + timezone.timedelta(days=1), tour)
day.save()
place = Venue("venueprueba", 3, "addressvenueprueba", s)
place.save()
g1 = Game(timezone.now(), tour, t1, t2, 1, day, place, 1)
g1.save()
g2 = Game(timezone.now()+timezone.timedelta(hours=2), tour, t1, t2, 2, day, place, 2)
g2.save()
