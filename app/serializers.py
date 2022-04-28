
from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import List,Item,Category



class UserSerializer(serializers.ModelSerializer):
    List = serializers.PrimaryKeyRelatedField(many=True,queryset=List.objects.all())
    class Meta:
        model = User
        fields = ['id','username','List']

class ItemSerializer(serializers.ModelSerializer):
    addedBy = serializers.ReadOnlyField(source = 'addedBy.username')
    class Meta :
        model = Item
        fields = ['itemName','isCompleted','addedBy']

class ItemReadSerializer(serializers.ModelSerializer):
    class Meta(ItemSerializer):
        deapth = 1

class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = '__all__'

class CategoryReadSerializer(serializers.ModelSerializer):
    class Meta(CategorySerializer):
        deapth = 1


class ListSerializer(serializers.ModelSerializer):
    class Meta :
        model = List
        fields = '__all__'

class ListReadSerializer(serializers.ModelSerializer):
    class Meta(ListSerializer):
        deapth = 1
