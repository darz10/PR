from django.test import TestCase

from django.urls import reverse
 
from .models import Impression
from login.models import Profile

 
 
class ImpressionTests(TestCase):
 
    def setUp(self):
        
        self.user = Profile.objects.create(
            username='Jok',
            password='12345'
        )
        self.user.save()

        self.impression = Impression.objects.create(
            name_impression='Lake',
            comment_impression='Nice place',
            location='Екатеринбург',
            user=self.user
        )

    
    def test_impression_create_view(self):
        """Тест на создание записи"""
        
        response = self.client.post(reverse('create_impression'), {
            'name_impression': 'New name',
            'comment_impression': 'New content',
            'location': 'New York',
            'user': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')
        self.assertContains(response, 'New York')
 

    
    def test_impression_update_view(self):
        """Тест на изменение записи"""
     
        response = self.client.post(reverse('update_impression', args='1'), {
            'name_impression': 'Update New name',
            'comment_impression': 'Update New content',
            'location': 'Москва',
            'user': self.user
        })
        self.assertEqual(response.status_code, 302)
 

    
    def test_post_delete_view(self):
        """Тест на удаление записи"""

        response = self.client.post(
            reverse('delete_impression', args='1'))
        self.assertEqual(response.status_code, 302)