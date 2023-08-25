from django.forms import ValidationError
from django.test import TestCase

from django101.testing.models import Profile


class ProfileModelTest(TestCase):
    def test_createProfile_whenValidEgn_should_succeed(self):
        egn = '1234567890'
        name = "Pesho"
        age = 19

        profile = Profile(
            name=name,
            age=age,
            egn=egn

        )
        profile.full_clean()
        profile.save()

    def test_createProfile_whenEgnContainsAlpha_shouldRaiseError(self):
        egn = '1234567a90'
        name = "Pesho"
        age = 19
        with self.assertRaises(ValidationError) as err:
            profile = Profile(
                name=name,
                age=age,
                egn=egn

            )
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(err.exception)

