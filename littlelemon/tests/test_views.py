from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title='Item 1', price=10.99, inventory=4)
        Menu.objects.create(title='Item 2', price=5.99, inventory=9)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        serialized_data = serializer.data
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)