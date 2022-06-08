from rest_framework import serializers

from .models import Barsa, Profile


class BarsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barsa
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
