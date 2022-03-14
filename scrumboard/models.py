from django.db import models

from scrumboard.managers.card_managers import CardManager
from scrumboard.managers.list_managers import Listanager

class List(models.Model):
    name = models.CharField(max_length=50)
    
    objects = models.Manager()
    manager = Listanager()
    
    def __str__(self):
        return f'List: {self.name}'

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    story_points = models.IntegerField(blank=True, null=True)
    business_value = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    manager = CardManager()

    def __str__(self):
        return f'Card: {self.title}'