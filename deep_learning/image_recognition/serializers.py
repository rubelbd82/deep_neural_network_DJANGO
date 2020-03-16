
from rest_framework import serializers

from .models import RecognizeModel

class RecognizeSerializer(serializers.Serializer):
    class Meta:
        model = RecognizeModel
        fields = ('id', 'name', 'description', 'image')