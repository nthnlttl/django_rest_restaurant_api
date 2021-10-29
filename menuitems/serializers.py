from rest_framework import serializers
from .models import Menuitems

class MenuitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menuitems
        fields = ('id', 'name', 'price', 'description')