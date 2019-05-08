from django.test import TestCase
from .models import Team,Category,Sex,State, Region

# Create your tests here.


#Test 6,14 Andres Quiroz
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




#Test 5,13 Andres Quiroz(TeamModel)


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

 # Cristian Test 1
class TestStateModel(TestCase):
    def test_create_state(self):
        s = State(id=1, name="Aguascalientes", code='esta1')
        s.save()

        estado1 = State.objects.get(id=1)
        self.assertEquals(estado1.pk, s.pk)
        self.assertEquals(estado1.pk, s.pk)

    # Cristian Test 2
    def test_delete_state(self):
        s = State(id=1, name="Aguascalientes", code='esta1')
        s.save()

        estado1 = State.objects.get(id=1)
        borrar = estado1.delete()
        self.assertTrue(borrar)
    # Cristian Test 3

    def test_edit_state(self):
        s = State(id=1, name="Aguascalientes", code='esta1')
        s.save()

        estado1 = State.objects.get(id=1)
        estado1.name="Tepito"
        estado1.save()
        self.assertEqual(State.objects.get(pk=1).name, "Tepito")

#Cristian Test 4


class RegionTest(TestCase):

    def test_delete_region(self):
        r1 = Region(id=1, name="Noreste", code="54545")
        r1.save()
        region2 = Region.objects.get(id=1)
        region2.save()
        delete=region2.delete()
        self.assertTrue(delete)
#Cristian Test 5

    def test_edit_region(self):
        r1 = Region(id=1, name="Noreste", code="54545")
        r1.save()
        region2 = Region.objects.get(id=1)
        region2.name="Norte"
        region2.save()
        self.assertEqual(Region.objects.get(pk=1).name, "Norte")