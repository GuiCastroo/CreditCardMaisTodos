import unittest
from src.domain.value_objects.cvv import Cvv
from pydantic.error_wrappers import ValidationError


class TestCvv(unittest.TestCase):
    def test_cvv_given_values_when_between_three_and_for_then_create_value_object(self):
        list_data = [3, 4]
        for valor in list_data:
            with self.subTest(valor=valor):
                data_with_three = Cvv(value=valor)
                exp = valor
                result = data_with_three.value
                self.assertEqual(exp, result)

    def test_cvv_given_values_when_is_different_three_and_for_then_not_create_value_object(self):
        list_data = [1, 2, 5, 6, 7, -2, -4, -5, 100]
        for valor in list_data:
            with self.subTest(valor=valor):
                with self.assertRaises(ValidationError):
                    Cvv(value=valor)



