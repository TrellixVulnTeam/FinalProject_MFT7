from django.test import TestCase

# Create your tests here.
from tabafi.models import Farmer


class FarmerTest(TestCase):

    def setUp(self):

        Farmer.objects.create(
            first_name='name1', last_name='last1', username='user1', phone_number='09133333333')
        Farmer.objects.create(
            first_name='name2', last_name='last2', username='user2', phone_number='09133333334')

    def test_puppy_breed(self):
        user1 = Farmer.objects.get(first_name='name1')
        user2 = Farmer.objects.get(first_name='name2')
        self.assertEqual(
            user1.id,1, "User1 belongs to Bull Dog breed.")
        self.assertEqual(
            user2.id,2,"User2 belongs to Gradane breed.")