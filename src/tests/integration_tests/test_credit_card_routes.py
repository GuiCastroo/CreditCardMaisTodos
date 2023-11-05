import unittest
import uuid

from fastapi.testclient import TestClient
from sqlalchemy import delete

from src.adapters.inbound.rest.main import app
from src.adapters.outbound.orm.database import Session
from src.adapters.outbound.orm.models import UserModel


class TestCreditCardRoutes(unittest.TestCase):
    identification = None

    @classmethod
    def setUpClass(cls):
        client = TestClient(app)
        cls.client = client
        test_user_credentials = {
            "username": "test_user",
            "password": "test_password"
        }
        form_data = {
            'grant_type': '',
            'username': 'test_user',
            'password': 'test_password',
            'scope': '',
            'client_id': '',
            'client_secret': ''
        }

        # Cabeçalhos da solicitação
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        client.post("auth/create-user", json=test_user_credentials)
        print("criamos user")
        response = client.post('/auth/token', data=form_data, headers=headers)
        print(f"pegamos token, {response.status_code}")
        token = response.json().get("access_token")
        cls.token = token

        cls.request_create_data = {
            "exp_date": "04/2030",
            "holder": "Gui",
            "number": "4539578763621486",
            "cvv": 123
        }

    def test_first_create_credit(self):
        response = self.client.post(
            "/credit-card", json=self.request_create_data, headers={"Authorization": f"Bearer {self.token}"}
        )
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.identification = response_data['identification']

    def test_get_one_credit_card_when_exist_id(self):
        response = self.client.get(f"/credit-card/", headers={"Authorization": f"Bearer {self.token}"})
        self.identification = response.json()["items"][0]["identification"]
        print(self.identification)
        response = self.client.get(
            f"/credit-card/{self.identification}", headers={"Authorization": f"Bearer {self.token}"}
        )

        self.assertEqual(response.status_code, 200)

    def test_get_one_credit_card_when_not_exist_id(self):
        non_existing_id = str(uuid.uuid4())
        response = self.client.get(f"/credit-card/{non_existing_id}", headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, 204)

    def test_get_all(self):
        response = self.client.get(f"/credit-card", headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls) -> None:
        async def cleanup_test_data():
            async with Session() as session:
                stmt = delete(UserModel).where(UserModel.username == "test_user")
                await session.execute(stmt)
                await session.commit()

        import asyncio
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cleanup_test_data())


if __name__ == '__main__':
    unittest.main()
