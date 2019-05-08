from django.test import TestCase

# Create your tests here.

from teams.models import Team, State,Category,Sex, Region
from users.models import Coach, Player,Scorekeeper
from tournaments.models import Tournament, Day, Game, Venue, Point, Foul, Win, Quarter
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth

def create_test_db():
    m = Sex.objects.create(name="Masculine")
    f = Sex.objects.create(name="Feminine")
    u15 = Category.objects.create(name='U-15')
    u17 = Category.objects.create(name='U-17')
    u19 = Category.objects.create(name='U-19')
    s = State.objects.create(name="Prueba", code="PRB")
    s.save()
    s2 = State.objects.create(name="Prueba2", code="PRB2")
    s2.save()
    r = Region.objects.create(name="PruebaR", code="PRBR")
    r.state_set.add(s)
    r.state_set.add(s2)
    t1 = Team.objects.create(sex=f, category=u15, state=s, address="addprueba1", name="teamprueba1")
    t1.save()
    t1.generate_code()
    t2 = Team.objects.create(sex=f, category=u15, state=s, address="addprueba2", name="teamprueba2")
    t2.save()
    t2.generate_code()
    t3 = Team.objects.create(sex=f, category=u15, state=s2, address="addprueba3", name="teamprueba3")
    t3.save()
    t3.generate_code()
    tour = Tournament.objects.create(is_active=True, sex=f, category=u15, name="tourprueba", start_date=timezone.now())
    tour.save()
    tour.team_set.add(t1)
    tour.team_set.add(t2)
    tour.team_set.add(t3)
    tour.save()
    day = Day.objects.create(number=1, is_inter_zone=False, start_date=timezone.now(),
                             end_date=timezone.now() + timezone.timedelta(days=1), tournament=tour)
    day.save()
    place = Venue.objects.create(name="venueprueba", courts=3, address="addressvenueprueba", state=s)
    place.save()
    g1 = Game.objects.create(number=1, date_time=timezone.now(), team_local=t1, team_visitor=t2, court=1, day=day,
                             venue=place)
    g1.save()
    g2 = Game.objects.create(number=2, date_time=timezone.now() + timezone.timedelta(hours=2), team_local=t1,
                             team_visitor=t2, court=2, day=day, venue=place)
    g2.save()
    up1 = User.objects.create_user(username='p1', email='p1@mail', password='pass', first_name="p1first",
                                   last_name="p1last")
    up2 = User.objects.create_user(username='p2', email='p2@mail', password='pass', first_name="p2first",
                                   last_name="p2last")
    uc1 = User.objects.create_user(username='c1', email='c1@mail', password='pass', first_name="c1first",
                                   last_name="c1last")
    uc2 = User.objects.create_user(username='c2', email='c2@mail', password='pass', first_name="c2first",
                                   last_name="c2last")
    c1 = Coach.objects.create(user=uc1, telephone="1234567890", start_date=timezone.now(), team=t1)
    c1.save()
    c2 = Coach.objects.create(user=uc2, telephone="1234567890", start_date=timezone.now(), team=t2)
    c2.save()
    p1 = Player.objects.create(sex=f, user=up1, date_of_birth=timezone.now(), telephone="12345667890", team=t1)
    p1.save()
    p2 = Player.objects.create(sex=f, user=up2, date_of_birth=timezone.now(), telephone="22345667890", team=t2)
    p2.save()
    q = Quarter.objects.create(game=g1, number=1)
    q2 = Quarter.objects.create(game=g1, number=2)
    q3 = Quarter.objects.create(game=g1, number=3)
    q4 = Quarter.objects.create(game=g1, number=4)
    Point.objects.create(quarter=q, player=p1, value=1)
    Point.objects.create(quarter=q, player=p2, value=2)
    Point.objects.create(quarter=q2, player=p1, value=1)
    Point.objects.create(quarter=q2, player=p2, value=1)
    Point.objects.create(quarter=q2, player=p1, value=1)
    Point.objects.create(quarter=q2, player=p2, value=1)
    Point.objects.create(quarter=q4, player=p1, value=1)
    Point.objects.create(quarter=q4, player=p2, value=1)
    Point.objects.create(quarter=q4, player=p1, value=1)
    Point.objects.create(quarter=q4, player=p2, value=1)
    Foul.objects.create(quarter=q, player=p1, type='1')
    Foul.objects.create(quarter=q, player=p2, type='1')
    g1.finish()


#
# class StatisticsViewTests(TestCase):
#     def test_non_existing(self):
#         response = self.client.get(
#             "/tournaments/stats/1/"
#         )
#         self.assertEqual(response.status_code, 404)
#
#     def test_empty(self):
#         tour = Tournament(1, name="tourprueba", start_date=timezone.now())
#         tour.save()
#         response = self.client.get(
#             "/tournaments/stats/1/"
#         )
#         self.assertContains(response, "This tournament has no played games")
#
#     def test_correct(self):
#         create_test_db()
#         response = self.client.get(
#             "/tournaments/stats/1/"
#         )
#         self.assertContains(response, "Standings")
#
#
# class GamesViewTests(TestCase):
#     def test_not_played(self):
#         create_test_db()
#         response = self.client.get(
#             "/tournaments/day/1/"
#         )
#         self.assertContains(response, "Not played yet")
#
#
#
#     def test_all_played(self):
#         create_test_db()
#         g2 = Game.objects.get(id=2)
#         g2.is_finished = True
#         g2.save()
#         response = self.client.get(
#             "/tournaments/day/1/"
#         )
#         self.assertNotContains(response, "Not played yet")
#         # self.assertNotContains(response, "None")
#
#     def test_no_games(self):
#         tour = Tournament(1, name="tourprueba", start_date=timezone.now())
#         tour.save()
#         day = Day(1, number=1, is_inter_zone=False, start_date=timezone.now(),
#                   end_date=timezone.now() + timezone.timedelta(days=1), tournament=tour)
#         day.save()
#         response = self.client.get(
#             "/tournaments/day/1/"
#         )
#         self.assertContains(response, "No games scheduled.")
#
#     def test_not_exists(self):
#         response = self.client.get(
#             "/tournaments/day/1/"
#         )
#         self.assertEqual(response.status_code, 404)
#
#
# class TournamentViews(TestCase):
#     def test_active_tournament(self):
#         create_test_db()
#         response = self.client.get(
#             "/tournaments/"
#         )
#         self.assertContains(response,"Active")
#
#
#
# class GameModelTests(TestCase):
#     def test_local_points(self):
#         create_test_db()
#         g = Game.objects.get(id=1)
#         self.assertEqual(g.get_local_points(), 1)
#
#     def test_visitor_points(self):
#         create_test_db()
#         g = Game.objects.get(id=1)
#         self.assertEqual(g.get_visitor_points(), 2)
#
#     def test_local_fouls(self):
#         create_test_db()
#         g = Game.objects.get(id=1)
#         self.assertEqual(g.get_local_fouls(), 1)
#
#     def test_visitor_fouls(self):
#         create_test_db()
#         g = Game.objects.get(id=1)
#         self.assertEqual(g.get_visitor_fouls(), 1)
#
#     def test_str(self):
#         create_test_db()
#         day = Day.objects.get(id=1)
#         t1 = Team.objects.get(id=1)
#         t2 = Team.objects.get(id=2)
#         venue = Venue.objects.get(id=1)
#         num = 3
#         (Game(3, number=num, date_time=timezone.now(), team_local=t1, team_visitor=t2, court=1, day=day, venue=venue))\
#             .save()
#         g = Game.objects.get(id=3)
#         self.assertEqual(str(g),
#                          "Game " + str(num) + " day " + str(day.number) + " of " + day.tournament.name + ": " + t1.name
#                          + " vs " + t2.name + " (not played yet)")
#
#     def test_str_finished(self):
#         create_test_db()
#         g = Game.objects.get(id=1)
#         self.assertEqual(str(g), "Game 1 day 1 of tourprueba: teamprueba1 vs teamprueba2 (finished)")
#
#     def test_str_changed(self):
#         create_test_db()
#         g = Game.objects.get(id=1)
#         g.team_visitor = Team.objects.get(id=3)
#         g.save()
#         g = Game.objects.get(id=1)
#         self.assertEqual(str(g), "Game 1 day 1 of tourprueba: teamprueba1 vs teamprueba3 (finished)")
#
#     def test_str_deleted(self):
#         create_test_db()
#         Game.objects.get(id=1).delete()
#         try:
#             g = Game.objects.get(id=1)
#         except Game.DoesNotExist:
#             self.assertEqual(True, True)
#             return
#         self.assertEqual(True, False)
#
#
# class FoulModelTests(TestCase):
#     def test_str(self):
#         create_test_db()
#         f = Foul.objects.get(id=1)
#         self.assertEqual(str(f), "")
#
#     def test_add(self):
#         create_test_db()
#         g = Game.objects.get(id=1)
#         p = Player.objects.get(id=1)
#         prev = Foul.objects.filter(game=g).count()
#         (Foul(3, game=g, player=p, type='1')).save()
#         curr = Foul.objects.filter(game=g).count()
#         self.assertEqual(prev + 1, curr)
#
#     def test_delete(self):
#         create_test_db()
#         g = Game.objects.get(id=1)
#         p = Player.objects.get(id=1)
#         prev = Foul.objects.filter(game=g).count()
#         Foul.objects.get(id=2).delete()
#         curr = Foul.objects.filter(game=g).count()
#         self.assertEqual(prev, curr + 1)
#
#     def test_edit(self):
#         create_test_db()
#         f = Foul.objects.get(id=1)
#         f.type = "2"
#         f.save()
#         self.assertEqual(Foul.objects.get(id=1).type, "2")


#AndresQuiroz Test 8,11  DayModel
class TestModelDay(TestCase):
    def test_created(self):
        User.objects.create_user(
            username="uname",
            email="uemail",
            password="upass",
            first_name="ufirst",
            last_name="ulast"
        )

        c = Category(1, name="U-15")
        c.save()
        sex = Sex(1, name="Feminine")
        sex.save()
        s = State(1, "Prueba", "PRB")
        s.save()
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1", category=c, sex=sex)
        tour1 = Tournament(id=1, name="TestName", start_date='2001-01-01', category=c, sex=sex, end_date='2001-01-01',
                           is_active=True)
        tour1.save()
        t1.save()
        t1.generate_code()


        d=Day(1,number=1,is_inter_zone=False,start_date='2001-01-01',end_date='2001-01-01',tournament=tour1)
        d.save()

        day = Day.objects.get(pk=1)
        self.assertEquals(day.pk,d.pk)

    def test_deleted(self):
        User.objects.create_user(
            username="uname",
            email="uemail",
            password="upass",
            first_name="ufirst",
            last_name="ulast"
        )

        c = Category(1, name="U-15")
        c.save()
        sex = Sex(1, name="Feminine")
        sex.save()
        s = State(1, "Prueba", "PRB")
        s.save()
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1", category=c, sex=sex)
        tour1 = Tournament(id=1, name="TestName", start_date='2001-01-01', category=c, sex=sex, end_date='2001-01-01',
                           is_active=True)
        tour1.save()
        t1.save()
        t1.generate_code()

        d = Day(1, number=1, is_inter_zone=False, start_date='2001-01-01', end_date='2001-01-01', tournament=tour1)
        d.save()

        day = Day.objects.get(pk=1)
        delete=day.delete()
        self.assertTrue(delete)

    # def test_all_played(self):
    #     create_test_db()
    #     g2 = Game.objects.get(id=2)
    #     g2.is_finished = True
    #     g2.save()
    #     response = self.client.get(
    #         "/tournaments/day/1/"
    #     )
    #     self.assertNotContains(response, "Not played yet")
    #     # self.assertNotContains(response, "None")
    #
    # def test_no_games(self):
    #     tour = Tournament(1, name="tourprueba", start_date=timezone.now())
    #     tour.save()
    #     day = Day(1, number=1, is_inter_zone=False, start_date=timezone.now(),
    #               end_date=timezone.now() + timezone.timedelta(days=1), tournament=tour)
    #     day.save()
    #     response = self.client.get(
    #         "/tournaments/day/1/"
    #     )
    #     self.assertContains(response, "No games scheduled.")

#AndresQuiroz Test 9,15  VenueModel
class testModelVenue(TestCase):
    def test_create(self):
        s = State(1, "Prueba", "PRB")
        s.save()

        v = Venue(1,name="prueba",courts=5,address="pruebaadd",state=s)
        v.save()
        venue = Venue.objects.get(pk=1)
        self.assertEquals(v.pk,venue.pk)

    def test_delete(self):
        s = State(1, "Prueba", "PRB")
        s.save()

        v = Venue(1,name="prueba",courts=5,address="pruebaadd",state=s)
        v.save()

        venue = Venue.objects.get(pk=1)
        delete=venue.delete()
        self.assertTrue(delete)

#AndresQuiroz Test 10  SexModel
class testSexModel(TestCase):
    def test_create(self):
        s = Sex(1,name="Feminine")
        s.save()

        sex=Sex.objects.get(pk=1)

        self.assertEquals(s.pk,sex.pk)

    def test_delete(self):
        s = Sex(1, name="Feminine")
        s.save()

        sex = Sex.objects.get(pk=1)
        delete=sex.delete()
        self.assertTrue(delete)

#AndresQuiroz Test 16  QuarterModel
class testQuarterModel(TestCase):
    def test_create(self):
        u = User.objects.create_user(
            username="uname",
            email="uemail",
            password="upass",
            first_name="ufirst",
            last_name="ulast"
        )

        c = Category(1, name="U-15")
        c.save()
        sex = Sex(1, name="Feminine")
        sex.save()
        s = State(1, "Prueba", "PRB")
        s.save()
        v = Venue(1, name="prueba", courts=5, address="pruebaadd", state=s)
        v.save()
        place = Venue.objects.get(pk=1)
        sc1=Scorekeeper(user=u,telephone='14321',state=s)
        sc1.save()
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1", category=c, sex=sex)
        t2 = Team(2, state=s, address="addprueba2", name="teamprueba2", category=c, sex=sex)
        tour1 = Tournament(id=1, name="TestName", start_date='2001-01-01', category=c, sex=sex, end_date='2001-01-01',
                           is_active=True)
        tour1.save()
        d = Day(1, number=1, is_inter_zone=False, start_date='2001-01-01', end_date='2001-01-01', tournament=tour1)
        d.save()
        day = Day.objects.get(pk=1)
        t1.save()
        t2.save()
        g1 = Game(1, number=1, date_time=timezone.now(), team_local=t1, team_visitor=t2, court=1, day=day, venue=place,scorekeeper=sc1,is_finished=False)
        g1.save()
        q = Quarter(id=1, number=1,game=g1)
        q.save()
        quarter=Quarter.objects.get(id=1)
        self.assertEquals(q.pk,quarter.pk)


class TeamViewTests(TestCase):
    def setUp(self):
        create_test_db()

    def test_not_logged(self):
        tour_id = Tournament.objects.first().id
        team_id = Team.objects.get(name="teamprueba1").id
        response = self.client.get("/tournaments/"+str(tour_id)+"/teams/"+str(team_id)+"/")
        self.assertEqual(response.status_code, 302)

    # view team code
    def test_logged(self):
        tour_id = Tournament.objects.first().id
        team_id = Team.objects.get(name="teamprueba1").id
        self.client.login(username="c1", password="pass")
        response = self.client.get("/tournaments/"+str(tour_id)+"/teams/"+str(team_id)+"/")
        code = Team.objects.get(id=team_id).code
        self.assertNotEqual(code, None)
        self.assertEqual(True, response.context["user"].is_authenticated)
        self.assertContains(response, code)

    # generate team code
    def test_generate(self):
        tour_id = Tournament.objects.first().id
        team_id = Team.objects.get(name="teamprueba1").id
        self.client.login(username="c1", password="pass")

        previous_code = Team.objects.get(id=team_id).code

        response = self.client.get("/tournaments/"+str(tour_id)+"/teams/"+str(team_id)+"/")

        self.assertContains(response, previous_code)

        self.client.get("/tournaments/"+str(tour_id)+"/teams/"+str(team_id)+"/regenerate/")

        current_code = Team.objects.get(id=team_id).code

        response = self.client.get("/tournaments/"+str(tour_id)+"/teams/"+str(team_id)+"/")

        self.assertNotEqual(previous_code, current_code)
        self.assertContains(response, current_code)

    # view players
    def test_correct(self):
        tour_id = Tournament.objects.first().id
        team_id = Team.objects.get(name="teamprueba1").id
        self.client.login(username="c1", password="pass")
        response = self.client.get("/tournaments/"+str(tour_id)+"/teams/"+str(team_id)+"/")
        self.assertEqual(True, response.context["user"].is_authenticated)
        self.assertContains(response, "p1first p1last")

    # remove player
    def test_remove(self):
        tour_id = Tournament.objects.first().id
        team_id = Team.objects.get(name="teamprueba1").id
        player_id = Player.objects.get(user__username="p1").id
        self.client.login(username="c1", password="pass")
        response = self.client.get("/tournaments/"+str(tour_id)+"/teams/"+str(team_id)+"/")
        self.assertContains(response, "p1first p1last")
        data = {
            "tournament": tour_id,
            "team": team_id,
            "player": player_id
        }
        self.client.get("/users/player/delete/secure/", data)
        response = self.client.get("/tournaments/"+str(tour_id)+"/teams/"+str(team_id)+"/")
        self.assertNotContains(response, "p1first p1last")

    def test_remove_not_logged(self):
        tour_id = Tournament.objects.first().id
        team_id = Team.objects.get(name="teamprueba1").id
        player_id = Player.objects.get(user__username="p1").id
        data = {
            "tournament": tour_id,
            "team": team_id,
            "player": player_id
        }
        response = self.client.get("/users/player/delete/secure/", data)
        self.assertEqual(response.status_code, 302)

    # coach views player
    def test_view_logged(self):
        tour_id = Tournament.objects.first().id
        team_id = Team.objects.get(name="teamprueba1").id
        player_id = Player.objects.get(user__username="p1").id
        self.client.login(username="c1", password="pass")
        response = self.client.get("/tournaments/" + str(tour_id) + "/teams/" + str(team_id) + "/")
        self.assertContains(response, "p1first p1last")
        response = self.client.get("/tournaments/" + str(tour_id) + "/teams/" + str(team_id) + "/player/"+str(player_id)+"/")
        self.assertContains(response, "p1first")

    # coach views player
    def test_view_not_logged(self):
        tour_id = Tournament.objects.first().id
        team_id = Team.objects.get(name="teamprueba1").id
        player_id = Player.objects.get(user__username="p1").id
        response = self.client.get(
            "/tournaments/" + str(tour_id) + "/teams/" + str(team_id) + "/player/" + str(player_id) + "/")
        self.assertEqual(response.status_code, 302)
