from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    memorable_word = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'memorable_word', 'image']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password2": "Passwords do not match."})

        if not data.get('memorable_word'):
            raise serializers.ValidationError({"memorable_word": "This field is required."})

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1']
        )

        Profile.objects.create(
            user=user,
            memorable_word=validated_data['memorable_word'],
            image=validated_data.get('image', 'default_profile_q35ywj')
        )

        return user
