from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model', 'description', 'Seats', 'Price', 'image']

