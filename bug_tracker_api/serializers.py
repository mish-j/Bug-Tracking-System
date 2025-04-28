# bug_tracker_api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Bug, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'role']

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'bug', 'author', 'author_name', 'text', 'created_at']
        read_only_fields = ['author']
    
    def get_author_name(self, obj):
        return obj.author.username
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class BugSerializer(serializers.ModelSerializer):
    reporter_name = serializers.SerializerMethodField()
    assignee_name = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Bug
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'reporter', 'reporter_name', 'assignee', 'assignee_name',
            'created_at', 'updated_at', 'comments'
        ]
        read_only_fields = ['reporter']
    
    def get_reporter_name(self, obj):
        return obj.reporter.username
    
    def get_assignee_name(self, obj):
        if obj.assignee:
            return obj.assignee.username
        return None
    
    def create(self, validated_data):
        validated_data['reporter'] = self.context['request'].user
        return super().create(validated_data)

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=UserProfile.USER_ROLES)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role']
    
    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, role=role)
        return user