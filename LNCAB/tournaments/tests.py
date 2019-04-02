from django.test import TestCase

# Create your tests here.

from teams.models import Team, State
from users.models import Coach, Player
from tournaments.models import Tournament, Day, Game, Venue, Point, Foul, Win
from django.utils import timezone
from django.contrib.auth.models import User


def create_test_db():
    s = State(1, "Prueba", "PRB")
    s.save()
    up1 = User.objects.create_user('p1', 'p1@mail', 'pass')
    up2 = User.objects.create_user('p2', 'p2@mail', 'pass')
    uc1 = User.objects.create_user('c1', 'c1@mail', 'pass')
    uc2 = User.objects.create_user('c2', 'c2@mail', 'pass')
    t1 = Team(1, state=s, address="addprueba1", name="teamprueba1")
    t1.save()
    t2 = Team(2, state=s, address="addprueba2", name="teamprueba2")
    t2.save()
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
    day = Day(1, number=1, is_inter_zone=False, start_date=timezone.now(),
              end_date=timezone.now() + timezone.timedelta(days=1), tournament=tour)
    day.save()
    place = Venue(1, name="venueprueba", courts=3, address="addressvenueprueba", state=s)
    place.save()
    g1 = Game(1, number=1, date_time=timezone.now(), team_local=t1, team_visitor=t2, court=1, day=day, venue=place)
    g1.save()
    g2 = Game(2, number=2, date_time=timezone.now() + timezone.timedelta(hours=2), team_local=t1, team_visitor=t2,
              court=2, day=day, venue=place)
    g2.save()
    g1.is_finished = True
    g1.save()
    (Point(1, game=g1, player=p1, value=1)).save()
    (Point(2, game=g1, player=p2, value=2)).save()
    (Foul(1, game=g1, player=p1, type='1')).save()
    (Foul(2, game=g1, player=p2, type='1')).save()
    (Win(1, team=t1, tournament=tour)).save()
    (Win(2, team=t2, tournament=tour)).save()
    (Win(3, team=t2, tournament=tour)).save()


class StatisticsViewTests(TestCase):
    def test_non_existing(self):
        response = self.client.get(
            "/tournaments/stats/1/"
        )
        self.assertEqual(response.status_code, 404)

    def test_empty(self):
        tour = Tournament(1, name="tourprueba", start_date=timezone.now())
        tour.save()
        response = self.client.get(
            "/tournaments/stats/1/"
        )
        self.assertContains(response, "This tournament has no played games")

    def test_correct(self):
        create_test_db()
        response = self.client.get(
            "/tournaments/stats/1/"
        )
        self.assertContains(response, "Standings")


class GamesViewTests(TestCase):
    def test_not_played(self):
        create_test_db()
        response = self.client.get(
            "/tournaments/day/1/"
        )
        self.assertContains(response, "Not played yet")

    def test_all_played(self):
        create_test_db()
        g2 = Game.objects.get(id=2)
        g2.is_finished = True
        g2.save()
        response = self.client.get(
            "/tournaments/day/1/"
        )
        self.assertNotContains(response, "Not played yet")

    def test_no_games(self):
        tour = Tournament(1, name="tourprueba", start_date=timezone.now())
        tour.save()
        day = Day(1, number=1, is_inter_zone=False, start_date=timezone.now(),
                  end_date=timezone.now() + timezone.timedelta(days=1), tournament=tour)
        day.save()
        response = self.client.get(
            "/tournaments/day/1/"
        )
        self.assertContains(response, "No games scheduled.")

    def test_not_exists(self):
        response = self.client.get(
            "/tournaments/day/1/"
        )
        self.assertEqual(response.status_code, 404)


class GameModelTests(TestCase):
    def test_local_points(self):
        create_test_db()
        g = Game.objects.get(id=1)
        self.assertEqual(g.get_local_points(), 1)

    def test_visitor_points(self):
        create_test_db()
        g = Game.objects.get(id=1)
        self.assertEqual(g.get_visitor_points(), 2)

    def test_local_fouls(self):
        create_test_db()
        g = Game.objects.get(id=1)
        self.assertEqual(g.get_local_fouls(), 1)

    def test_visitor_fouls(self):
        create_test_db()
        g = Game.objects.get(id=1)
        self.assertEqual(g.get_visitor_fouls(), 1)


