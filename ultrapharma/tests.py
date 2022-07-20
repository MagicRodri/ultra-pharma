from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
import os

class UltraPharmaConfigTest(TestCase):
    #
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('SECRET_KEY') 
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Weak secret key"
            self.fail(msg)

    # Run test with manage.py test