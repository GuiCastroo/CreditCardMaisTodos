import unittest
from src.domain.value_objects.cvv import Cvv
from pydantic.error_wrappers import ValidationError


class TestCvv(unittest.TestCase):
    def test_cvv_given_values_when_between_100_and_9999_then_create_value_object(self):
        valid_values = [100, 999, 1000, 9999]
        for value in valid_values:
            with self.subTest(value=value):
                data = Cvv(value=value)
                exp = value
                result = data.value
                self.assertEqual(exp, result)

    def test_cvv_given_values_when_not_between_100_and_9999_then_raise_validation_error(self):
        invalid_values = [1, 99, 10000, 100000, -100, -99]
        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaises(ValidationError):
                    Cvv(value=value)

if __name__ == '__main__':
    unittest.main()
