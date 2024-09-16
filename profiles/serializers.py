from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    memorable_word = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField()
    image = serializers.ImageField()

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2',
            'memorable_word', 'image'
        ]

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                {"password2": "Passwords do not match."}
            )
        if not data.get('memorable_word'):
            raise serializers.ValidationError(
                {"memorable_word": "This field is required."}
            )
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


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()
    is_superuser = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.user

    def get_is_admin(self, obj):
        return obj.user.is_staff

    def get_is_superuser(self, obj):
        return obj.user.is_superuser

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'memorable_word', 'image',
            'is_owner', 'is_admin', 'is_superuser'
        ]
