import unittest
from src.domain.value_objects.expiration_date import ExpirationDate


class TestExpirationDate(unittest.TestCase):
    def test_given_valid_data_when_exp_date_is_ok_then_return_correct_date(self):
        data = ExpirationDate(exp_date="2030-02")
        exp = data.exp_date
        result = "2030-02-28"
        self.assertEqual(exp, result)

    def test_given_valid_data_when_leap_year_then_return_correct_date(self):
        data = ExpirationDate(exp_date="2024-02")
        exp = data.exp_date
        result = "2024-02-29"
        self.assertEqual(exp, result)

    def test_given_invalid_data_when_exp_date_is_passed_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            ExpirationDate(exp_date="2022-13")

    def test_given_expired_data_when_exp_date_is_passed_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            ExpirationDate(exp_date="2020-05")

    def test_given_incorrect_format_data_when_exp_date_is_passed_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            ExpirationDate(exp_date="02/2022")


if __name__ == '__main__':
    unittest.main()
