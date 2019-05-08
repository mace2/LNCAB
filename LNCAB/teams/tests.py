from django.test import TestCase
from .models import Team,Category,Sex,State,Zone,Region

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

#Edit test Manuel García
    def test_edit_category(self):
        c = Category(id=1, name="U-15")
        c.save()

        category = Category.objects.get(id=1)
        category.name = "U-18"
        category.save()
        self.assertEquals(category.name, "U-18")
# Zone US test Manuel Garcia

class ZoneTest(TestCase):
    def test_create_zone(self):
        z = Zone(id=1, name="Suroeste", code="54545")
        z.save()

        zone = Zone.objects.get(id=1)
        self.assertEquals(zone.pk, z.pk)

    def test_delete_zone(self):
        z = Zone(id=1, name="Suroeste", code="54545")
        z.save()

        zone = Zone.objects.get(id=1)
        delete=zone.delete()
        self.assertTrue(delete)

    def test_edit_zone(self):
        z = Zone(id=1, name="Suroeste", code="54545")
        z.save()

        zone = Zone.objects.get(id=1)
        zone.name = "Noroeste"
        zone.save()
        self.assertEquals(zone.name, "Noroeste")

#Region US test Manuel García

class RegionTest(TestCase):
    def test_create_region(self):
        r = Region(id=1, name="centro", code="54545")
        r.save()

        region = Region.objects.get(id=1)
        self.assertEquals(region.pk, r.pk)

    def test_delete_region(self):
        r = Region(id=1, name="centro", code="54545")
        r.save()

        region = Region.objects.get(id=1)
        delete = region.delete()
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
#Delete team test Manuel Garcia
    def test_check_deleted(self):
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
        delete = team.delete()
        self.assertTrue(delete)









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

