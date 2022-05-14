from rest_framework import serializers

from .models import Barsa


class BarsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barsa
        fields = '__all__'
