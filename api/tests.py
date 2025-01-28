from rest_framework.test import APITestCase
from django.urls import reverse


class DataViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("api:data")
        
    def test(self):
        for i in range(30):
            response = self.client.get(self.url)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.status_code, 200)
        
    def tearDown(self):
        return super().tearDown()