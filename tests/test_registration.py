from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser


class UserRegistrationTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_registration(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('register'), data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!',
            'first_name': 'dummy_fake_name',
            'last_name': 'dummy_last_name',
            'phone_number': '+48000000000',
            'postal_code': '00-950',
            'town_name': 'Warsaw'
        })
        self.assertEqual(response.status_code, 302)

        user = CustomUser.objects.get(username='testuser')
        self.assertTrue(user.check_password('Testpass123!'))

    def test_user_registration_with_existing_username(self):
        CustomUser.objects.create_user(username='existinguser', password='testpass123')
        response = self.client.post(reverse('register'), data={
            'username': 'existinguser',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A user with that username already exists.')


'''
    def test_user_registration_with_invalid_data(self):
        response = self.client.post(reverse('register'), data={
            'username': '',
            'email': 'invalid email',
            'password1': 'short',
            'password2': 'mismatch'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required')
        self.assertContains(response, 'Enter a valid email address')
        self.assertContains(response, 'Ensure this value has at least 8 characters (it has 5).')
        self.assertContains(response, 'The two password fields did not match')
'''
