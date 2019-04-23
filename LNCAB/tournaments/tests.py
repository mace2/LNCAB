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
    s2 = State(2, "Prueba2", "PRB2")
    s2.save()
    t1 = Team(1, state=s, address="addprueba1", name="teamprueba1")
    t1.save()
    t1.generate_code()
    t2 = Team(2, state=s, address="addprueba2", name="teamprueba2")
    t2.save()
    t2.generate_code()
    t3 = Team(3, state=s2, address="addprueba3", name="teamprueba3")
    t3.save()
    t3.generate_code()
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
    tour.team_set.add(t3)
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
    (Point(1, game=g1, player=p1, value=1)).save()
    (Point(2, game=g1, player=p2, value=2)).save()
    (Foul(1, game=g1, player=p1, type='1')).save()
    (Foul(2, game=g1, player=p2, type='1')).save()
    g1.finish()


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
        # self.assertNotContains(response, "None")

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

    def test_str(self):
        create_test_db()
        day = Day.objects.get(id=1)
        t1 = Team.objects.get(id=1)
        t2 = Team.objects.get(id=2)
        venue = Venue.objects.get(id=1)
        num = 3
        (Game(3, number=num, date_time=timezone.now(), team_local=t1, team_visitor=t2, court=1, day=day, venue=venue))\
            .save()
        g = Game.objects.get(id=3)
        self.assertEqual(str(g),
                         "Game " + str(num) + " day " + str(day.number) + " of " + day.tournament.name + ": " + t1.name
                         + " vs " + t2.name + " (not played yet)")

    def test_str_finished(self):
        create_test_db()
        g = Game.objects.get(id=1)
        self.assertEqual(str(g), "Game 1 day 1 of tourprueba: teamprueba1 vs teamprueba2 (finished)")

    def test_str_changed(self):
        create_test_db()
        g = Game.objects.get(id=1)
        g.team_visitor = Team.objects.get(id=3)
        g.save()
        g = Game.objects.get(id=1)
        self.assertEqual(str(g), "Game 1 day 1 of tourprueba: teamprueba1 vs teamprueba3 (finished)")

    def test_str_deleted(self):
        create_test_db()
        Game.objects.get(id=1).delete()
        try:
            g = Game.objects.get(id=1)
        except Game.DoesNotExist:
            self.assertEqual(True, True)
            return
        self.assertEqual(True, False)


class FoulModelTests(TestCase):
    def test_str(self):
        create_test_db()
        f = Foul.objects.get(id=1)
        self.assertEqual(str(f), "")

    def test_add(self):
        create_test_db()
        g = Game.objects.get(id=1)
        p = Player.objects.get(id=1)
        prev = Foul.objects.filter(game=g).count()
        (Foul(3, game=g, player=p, type='1')).save()
        curr = Foul.objects.filter(game=g).count()
        self.assertEqual(prev + 1, curr)

    def test_delete(self):
        create_test_db()
        g = Game.objects.get(id=1)
        p = Player.objects.get(id=1)
        prev = Foul.objects.filter(game=g).count()
        Foul.objects.get(id=2).delete()
        curr = Foul.objects.filter(game=g).count()
        self.assertEqual(prev, curr + 1)

    def test_edit(self):
        create_test_db()
        f = Foul.objects.get(id=1)
        f.type = "2"
        f.save()
        self.assertEqual(Foul.objects.get(id=1).type, "2")
