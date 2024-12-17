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
    # Table to store annotations for each image.
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='annotations')
    label = models.CharField(max_length=100)  # e.g., 'Car', 'Person', 'Dog', etc.
    x_min = models.FloatField()
    y_min = models.FloatField()
    x_max = models.FloatField()
    y_max = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.label} on {self.image.name}'
