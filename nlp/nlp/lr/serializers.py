from rest_framework import serializers
from . models import endpoint


class endpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = endpoint
        fields = '__all__'
