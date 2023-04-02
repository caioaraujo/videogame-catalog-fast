import unittest

from fastapi.testclient import TestClient

from src.catalog import api

client = TestClient(api.app)


class TestApi(unittest.TestCase):

    def test_get(self):
        response = client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual("Under construction", response.json())

    def test_fetch_game(self):
        response = client.get("/games/1")
        self.assertEqual(200, response.status_code)
        self.assertEqual("Game id: 1", response.json())
