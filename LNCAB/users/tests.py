from django.test import TestCase
from django.utils import timezone

from teams.models import Team, State,Category,Sex
from users.models import Coach, Player
from tournaments.models import Tournament, Day, Game, Venue, Point, Foul, Win
from django.contrib.auth.models import User
from .forms import UserForm,LoginForm
from .forms import PlayerForm


# Create your tests here.


# class CoachModelTests(TestCase):
#     def test_create_coach(self):
#         # start = timezone.now()
#         # name = "Juan"
#         # last_names = "López Pérez"
#         # telephone = "
#         1234567890"
#         # email = "juanlopezperez@mail.com"
#         # (Coach(name=name, last_names=last_names, start_date=start, telephone=telephone, email_address=email)).save()
#         # self.assertIs(Coach.objects.filter(
#         #     name=name,
#         #     last_names=last_names,
#         #     start_date=start, telephone=telephone,
#         #     email_address=email
#         # ).count() > 0, True)
#         pass


#class PlayerFormTests(TestCase):
 #   def test_create(self):
  #      u = User.objects.create_user(
   #         username="uname",
    #        email="uemail",
     #       password="upass",
      #      first_name="ufirst",
       #     last_name="ulast"
        #)
        #self.client.force_login(u)
        #s = State(1, "Prueba", "PRB")
        #s.save()
        #t1 = Team(1, state=s, address="addprueba1", name="teamprueba1")
        #t1.save()
        #t1.generate_code()
        #data = {
         #   "code": t1.code,
          #  "date_of_birth": "01/15/2001",
           # "telephone": "1234567890",
            #"sex": "F"
        #}
        #self.client.post("/users/playerform.html/", data)
        #p = Player.objects.get(id=1)
        #self.assertEqual(str(p), u.first_name + " " + u.last_name)



#Andres Quiroz Test 1(User Form)
class UserFormTests(TestCase):
    def test_create(self):
        u = User.objects.create_user(
            id=1,
            username="uname",
            email="uemail",
            password="upass",
            first_name="ufirst",
            last_name="ulast"
        )

        us = User.objects.get(id=1)
        self.assertEqual(str(us), u.username)

    def test_form_valid_password(self):
         data = UserForm({
            "username" :"usname",
            "first_name" : "uname",
            "last_name" : "lname",
            "email" : "umail@mail.itesm.mx",
            "password": "upass",
            "password2":"upass",
         })

         self.assertTrue(data.is_valid())

    def test_form_not_valid_password(self):
         data = UserForm({
            "username" :"usname",
            "first_name" : "uname",
            "last_name" : "lname",
            "email" : "umail@mail.itesm.mx",
            "password": "upass",
            "password2":"upass2",
         })

         self.assertFalse(data.is_valid())

#AndresQuirozTest2(Login_Form) LE FALTA
class Login_Test(TestCase):
    def setUp(self):
        u=User.objects.create_user(
            id = 1,
            username="uname",
            email="uemail",
            password="upass",
            first_name="ufirst",
            last_name="ulast"
        )


        c = Category(1,name="U-15")
        c.save()
        sex= Sex(1,name="Feminine")
        sex.save()
        s = State(1, "Prueba", "PRB")
        s.save()
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1",category=c ,sex=sex)
        t1.save()
        t2 = Team(2, state=s, address="addprueba2", name="teamprueba2", category=c, sex=sex)
        t2.save()
        t1.generate_code()
        t2.generate_code()
        p1=Player(user=u ,team=t1, date_of_birth="2001-01-01",telephone="123456",sex=sex)

        tour1 = Tournament(id=1,name="TestName",start_date='2001-01-01',category=c,sex=sex,end_date='2001-01-01', is_active=True)


        day1 = Day(number=1, is_inter_zone=False, start_date="2001-01-01", end_date="2002-02-02", tournament=tour1)
        day1.save
        tour1.team_set.add(t1)
        tour1.team_set.add(t2)
        tour1.save()
        p1.save()



    def test_form(self):
        data = {
            "username" : "uname",
            "password" : "upass",

        }
        response=self.client.post('/users/login.html/',data)

        #self.assertRedirects(response,'/tournaments/1/day/1')
        self.assertTrue(response)



    def test_authentification_valid(self):
        #response = self.client.get(
         #   "/tournaments/1/day/1/"
        #)


        loginresponse=self.client.login(username='uname', password='upass')
        self.assertTrue(loginresponse)
        #self.assertEquals(response.status_code, 200)



    def test_authentification_invalid(self):
        loginresponse = self.client.login(username='unme', password='upass')
        self.assertFalse(loginresponse)


#AndresQuiroz  Test3(Same Sex Player and Team)
class Check_Same_Sex_Team_Player(TestCase):
    def setUp(self):
        u=User.objects.create_user(
            username="uname",
            email="uemail",
            password="upass",
            first_name="ufirst",
            last_name="ulast"
        )


        c = Category(1,name="U-15")
        c.save()
        sex= Sex(1,name="Feminine")
        sex.save()
        s = State(1, "Prueba", "PRB")
        s.save()
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1",category=c ,sex=sex)
        t1.save()
        t1.generate_code()
        p1=Player(user=u ,team=t1, date_of_birth="2001-01-01",telephone="123456",sex=sex)
        p1.save()


    def test_check_sex(self):
        t1=Team.objects.get(id=1)
        p1=Player.objects.get(id=1)
        self.assertEqual(t1.sex,p1.sex)


#AndresQuiroz  Test 4(Same Sex and category Tournament and Team)
class Check_Same_Sex_Category_Team_Tournament(TestCase):
    def setUp(self):
        u=User.objects.create_user(
            username="uname",
            email="uemail",
            password="upass",
            first_name="ufirst",
            last_name="ulast"
        )


        c = Category(1,name="U-15")
        c.save()
        sex= Sex(1,name="Feminine")
        sex.save()
        s = State(1, "Prueba", "PRB")
        s.save()
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1",category=c ,sex=sex)
        tour1 = Tournament(id=1, name="TestName", start_date='2001-01-01', category=c, sex=sex, end_date='2001-01-01',is_active=True)
        tour1.save()
        t1.save()
        t1.generate_code()



    def test_check_sex(self):
        t1=Team.objects.get(id=1)
        tour1=Tournament.objects.get(id=1)
        self.assertEqual(tour1.sex,t1.sex)
        self.assertEqual(tour1.category, t1.category)


#Andres Quiroz Test 7,12 Create Coach
class CoachModel(TestCase):
    def test_created(self):
        u=User.objects.create_user(
            username="uname",
            email="uemail",
            password="upass",
            first_name="ufirst",
            last_name="ulast"
        )

        c = Category(1,name="U-15")
        c.save()
        sex= Sex(1,name="Feminine")
        sex.save()
        s = State(1, "Prueba", "PRB")
        s.save()
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1",category=c ,sex=sex)
        t1.save()
        t1.generate_code()
        coa = Coach(id=1,user=u,telephone="2345678",start_date='2012-01-01',end_date='2012-10-10',team=t1)
        coa.save()


        coach = Coach.objects.get(pk=1)
        self.assertEquals(coa.pk,coach.pk)

    def test_deleted(self):
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
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1", category=c, sex=sex)
        t1.save()
        t1.generate_code()
        coa = Coach(id=1, user=u, telephone="2345678", start_date='2012-01-01', end_date='2012-10-10', team=t1)
        coa.save()
        precoach = Coach.objects.get(pk=1)
        delete=precoach.delete()
        self.assertTrue(delete)
















