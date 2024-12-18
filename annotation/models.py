# annotations/models.py
from django.db import models

class Image(models.Model):
    # Table to store uploaded images.
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=500, null=True, blank=True)  # URL field to store the image link
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Annotation(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='annotations')
    label = models.CharField(max_length=100)  # 'text' in the frontend data
    x = models.FloatField(null=True)  # x-coordinate from geometry
    y = models.FloatField(null=True)  # y-coordinate from geometry
    width = models.FloatField(null=True)  # width from geometry
    height = models.FloatField(null=True)  # height from geometry
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.label} on {self.image.name}'