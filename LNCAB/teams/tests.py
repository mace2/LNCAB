from django.test import TestCase
from .models import Team,Category,Sex,State

# Create your tests here.


#Test 6 Andres Quiroz
class TestCategoryModel(TestCase):
    def test_create_category(self):
        c = Category(id=1, name="U-15")
        c.save()

        category = Category.objects.get(id=1)
        self.assertEquals(category.pk,c.pk)

    def test_delete_category(self):
        c = Category(id=1, name="U-15")
        c.save()

        category = Category.objects.get(id=1)
        delete=category.delete()
        self.assertTrue(delete)




#Test 5 Andres Quiroz(TeamModel)
class CreateTeamTest(TestCase):
    def test_check_created(self):
        c = Category(id=1, name="U-15")
        c.save()
        sex = Sex(id=1, name="Feminine")
        sex.save()
        s = State(1, "Prueba", "PRB")
        s.save()
        t1 = Team(id=1, state=s, address="addprueba1", name="teamprueba1", category=c, sex=sex)
        t1.save()
        t1.generate_code()


        team = Team.objects.get(id=1)
        self.assertEquals(team.id,t1.id)


#class TeamModelTests(TestCase):
 #   def test_generate_code(self):
  #      from teams.models import Team, State
   #     s = State(1, "Prueba", "PRB")

       # s.save()
        #t1 = Team(1, state=s, address="addprueba1", name="teamprueba1")
       # t1.save()
        #t1.generate_code()
        #a = t1.code
        #t1.generate_code()
        #b = t1.code
        #self.assertNotEqual(a, b)

