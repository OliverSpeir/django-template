from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=256)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image_url = models.URLField(default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
