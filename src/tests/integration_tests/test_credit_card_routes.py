import unittest
from fastapi.testclient import TestClient
from src.adapters.inbound.rest.main import app
import uuid


class TestCreditCardRoutes(unittest.TestCase):
    identification = None

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)
        cls.request_create_data = {
            "exp_date": "04/2030",
            "holder": "Gui",
            "number": "4539578763621486",
            "cvv": 123
        }

    def test_first_create_credit(self):
        response = self.client.post("/credit-card", json=self.request_create_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.identification = response_data['identification']

    def test_get_one_credit_card_when_exist_id(self):
        response = self.client.get(f"/credit-card/")
        self.identification = response.json()["items"][0]["identification"]
        print(self.identification)
        response = self.client.get(f"/credit-card/{self.identification}")

        self.assertEqual(response.status_code, 200)

    def test_get_one_credit_card_when_not_exist_id(self):
        non_existing_id = str(uuid.uuid4())
        response = self.client.get(f"/credit-card/{non_existing_id}")
        self.assertEqual(response.status_code, 204)

    def test_get_all(self):
        response = self.client.get(f"/credit-card")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
