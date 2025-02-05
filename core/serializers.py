from rest_framework_mongoengine import serializers
from .models import Item

class ItemSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Item
        fields = '__all__' 