from django.test import TestCase
from django.utils import timezone

from teams.models import Team, State
from users.models import Coach, Player
from tournaments.models import Tournament, Day, Game, Venue, Point, Foul, Win
from django.contrib.auth.models import User
from .forms import PlayerForm


# Create your tests here.


# class CoachModelTests(TestCase):
#     def test_create_coach(self):
#         # start = timezone.now()
#         # name = "Juan"
#         # last_names = "López Pérez"
#         # telephone = "1234567890"
#         # email = "juanlopezperez@mail.com"
#         # (Coach(name=name, last_names=last_names, start_date=start, telephone=telephone, email_address=email)).save()
#         # self.assertIs(Coach.objects.filter(
#         #     name=name,
#         #     last_names=last_names,
#         #     start_date=start, telephone=telephone,
#         #     email_address=email
#         # ).count() > 0, True)
#         pass


class PlayerFormTests(TestCase):
    def test_create(self):
        u = User.objects.create_user(
            username="uname",
            email="uemail",
            password="upass",
            first_name="ufirst",
            last_name="ulast"
        )
        self.client.force_login(u)
        s = State(1, "Prueba", "PRB")
        s.save()
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1")
        t1.save()
        t1.generate_code()
        data = {
            "code": t1.code,
            "date_of_birth": "01/15/2001",
            "telephone": "1234567890",
            "sex": "F"
        }
        self.client.post("/users/playerform.html/", data)
        p = Player.objects.get(id=1)
        self.assertEqual(str(p), u.first_name + " " + u.last_name)



