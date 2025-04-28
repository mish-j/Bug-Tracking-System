# bug_tracker_api/views.py

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile, Bug, Comment
from .serializers import (
    UserSerializer, UserProfileSerializer, BugSerializer, 
    CommentSerializer, UserRegistrationSerializer
)
from .permissions import IsAdminOrReadOnly, IsAdminOrDeveloperOrReadOnly, IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all().order_by('-created_at')
    serializer_class = BugSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Bug.objects.all().order_by('-created_at')
        status = self.request.query_params.get('status')
        priority = self.request.query_params.get('priority')
        assigned_to = self.request.query_params.get('assigned_to')
        
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
        if assigned_to:
            queryset = queryset.filter(assignee=assigned_to)
            
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        queryset = Comment.objects.all().order_by('-created_at')
        bug_id = self.request.query_params.get('bug')
        
        if bug_id:
            queryset = queryset.filter(bug_id=bug_id)
            
        return queryset

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]