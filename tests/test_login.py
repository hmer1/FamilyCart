from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser


class UserLoginTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='Testpass123!')

    def test_user_login(self):
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('user_login'), data={
            'username': 'testeruser',
            'password': 'Testpass123!'
        })
        self.assertEqual(response.status_code, 200)

        user = CustomUser.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)