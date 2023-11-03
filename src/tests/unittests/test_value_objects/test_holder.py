import unittest
from pydantic import ValidationError
from src.domain.value_objects.holder import Holder


class TestHolder(unittest.TestCase):
    def test_given_valid_name_when_creating_holder_then_name_is_in_uppercase(self):
        valid_name = "john"
        holder = Holder(name=valid_name)
        self.assertEqual(holder.name, valid_name.upper())

    def test_given_name_with_less_than_3_characters_when_creating_holder_then_validation_error(self):
        invalid_name = "jo"
        with self.assertRaises(ValidationError):
            Holder(name=invalid_name)

    def test_given_empty_name_when_creating_holder_then_validation_error(self):
        empty_name = None
        with self.assertRaises(ValidationError):
            Holder(name=empty_name)


if __name__ == '__main__':
    unittest.main()
