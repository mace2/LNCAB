from django.test import TestCase
from .models import Coach
from django.utils import timezone

# Create your tests here.


class CoachModelTests(TestCase):
    def test_create_coach(self):
        start = timezone.now()
        name = "Juan"
        last_names = "López Pérez"
        telephone = "1234567890"
        email = "juanlopezperez@mail.com"
        (Coach(name=name, last_names=last_names, start_date=start, telephone=telephone, email_address=email)).save()
        self.assertIs(Coach.objects.filter(
            name=name,
            last_names=last_names,
            start_date=start, telephone=telephone,
            email_address=email
        ).count() > 0, True)

