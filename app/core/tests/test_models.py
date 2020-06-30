from django.test import TestCase
from django.contrib.auth import get_user_model


class MeodelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test creating a new user with email is successufull"""
        email = 'root@root.com'
        password = 'testing321'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
