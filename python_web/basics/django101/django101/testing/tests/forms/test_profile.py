from django.forms import ValidationError
from django.test import TestCase

from django101.testing.forms.profile import ProfileForm
from django101.testing.models import Profile


class ProfileModelTest(TestCase):
    def test_saveProfileForm_whenValidEgn_shouldBeValid(self):
        egn = '1234567890'
        name = "Pesho"
        age = 19

        form = ProfileForm(data={'name': name,
                                 'age': age,
                                 'egn': egn}
                           )

        self.assertTrue(form.is_valid())

    def test_whenAlphaInEgn_formIsInvalid(self):
        egn = '12345678a0'
        name = "Pesho"
        age = 19
        form = ProfileForm(data={'name': name,
                                 'age': age,
                                 'egn': egn}
                           )

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_eng11digits_shouldInvalid(self):
        egn = '12345678901'
        name = "Pesho"
        age = 19

        form = ProfileForm(data={'name': name,
                                 'age': age,
                                 'egn': egn}
                           )

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_eng9digits_shouldInvalid(self):
        egn = '123456789'
        name = "Pesho"
        age = 19

        form = ProfileForm(data={'name': name,
                                 'age': age,
                                 'egn': egn}
                           )

        self.assertFalse(form.is_valid())
