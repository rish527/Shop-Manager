from rest_framework import serializers
from .models import Shop

class ShopSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=['name','latitude','longitude']
