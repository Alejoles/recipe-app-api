"""
    Test for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Test models. """

    def test_create_user_with_email_successful(self):
        """ Test creating an user with an email is successful. """
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,        # noqa
            password = password,  # noqa
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
