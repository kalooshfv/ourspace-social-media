from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    creator_username = serializers.CharField(source='creator.username')
    creator_image = serializers.CharField(source='creator.image')
    class Meta:
        model = Post
        fields = ('id', 'content', 'creator', 'date', 'creator_username', 'creator_image')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'image', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            image=validated_data.get('image', None),
            password=validated_data['password']
        )
        return user


