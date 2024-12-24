from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    
    def setUp(self):
        
        self.client = APIClient()
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        
        self.menu1 = Menu.objects.create(title="TceCream", price=80, inventory = 100)
        self.menu2 = Menu.objects.create(title="PanCake", price=50, inventory = 150)
        self.menu3 = Menu.objects.create(title="LemonJuice", price=30, inventory = 40)
        
        self.url = reverse('menu')
        
    def test_getall(self):
        response = self.client.get(self.url)
        
        
        expected_data = MenuSerializer([self.menu1, self.menu2 ,self.menu3], many=True).data
        
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)