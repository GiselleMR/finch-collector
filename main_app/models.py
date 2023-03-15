from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    

    def __str__(self) -> str:
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('details', kwargs={'cat_id: self.id'})
