from .models import client

from rest_framework import serializers

class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = ("__all__")