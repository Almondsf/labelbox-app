from rest_framework import serializers
from annotation.models import Image, Annotation

class ImageSerializer(serializers.ModelSerializer):
    # Serializer for the Image model.
    class Meta:
        model = Image
        fields = ['id', 'name', 'image_url', 'uploaded_at']


class AnnotationSerializer(serializers.ModelSerializer):
    # Serializer for the Annotation model.
    class Meta:
        model = Annotation
        fields = ['id', 'image', 'label', 'x_min', 'y_min', 'x_max', 'y_max', 'created_at']
