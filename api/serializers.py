from rest_framework import serializers
from azure.models import resource, resourcegroup, Hero

class resourcegroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = resourcegroup
        fields = ('__all__')

class resourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = resource
        fields = ('__all__')
        
class heroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('__all__')