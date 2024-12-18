from rest_framework import viewsets
from annotation.models import Image, Annotation
from annotation.serializers import ImageSerializer, AnnotationSerializer
from django.http import JsonResponse    
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    