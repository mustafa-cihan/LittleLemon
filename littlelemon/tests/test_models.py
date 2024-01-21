from django.test import TestCase
from restaurant.models import Menu


class MenuTestCase(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(title='Test Menu Item', price=10.99, inventory=10)
        self.assertEqual(menu.title, 'Test Menu Item')
        self.assertEqual(menu.price, 10.99)
        self.assertEqual(menu.inventory, 10)
        self.assertEqual(str(menu), 'Test Menu Item : 10.99')