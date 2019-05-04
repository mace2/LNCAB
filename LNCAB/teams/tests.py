from django.test import TestCase

# Create your tests here.


class TeamModelTests(TestCase):
    def test_generate_code(self):
        from teams.models import Team, State
        s = State(1, "Prueba", "PRB")
        s.save()
        t1 = Team(1, state=s, address="addprueba1", name="teamprueba1")
        t1.save()
        t1.generate_code()
        a = t1.code
        t1.generate_code()
        b = t1.code
        self.assertNotEqual(a, b)

