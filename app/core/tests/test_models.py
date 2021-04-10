from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating is done
        """
        email = 'test@gmail.com'
        password = '12345Test'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalise_email(self):
        email = "suamnta9090@GMAIL.com"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_new_superUSER(self):
        user = get_user_model().objects.create_superuser("admin@admin.com", "test123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
