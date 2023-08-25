from unittest import TestCase

from django.core.exceptions import ValidationError

from django101.testing.validators import contains_only_digits_validator


class ContainsOnlyDigitsValidator(TestCase):
    def test_validate_whenOnlyDigits(self):
        contains_only_digits_validator('123')
        # self.assertTrue(True)c

    def test_validate_whenEmpty(self):
        contains_only_digits_validator('')
        # self.assertTrue(True)

    def test_validate_whenContainAlpha_shouldRaise(self):
        with self.assertRaises(ValidationError) as err:
            contains_only_digits_validator('1a23')
        self.assertIsNotNone(err.exception)