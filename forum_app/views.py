from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from forum_app.models import Comment, Post
from forum_app.permissions import IsOwnerOrReadOnly
from forum_app.serializers import CommentSerializer, PostSerializer
from forum_app.throttling import PostThrottle


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [PostThrottle, AnonRateThrottle, UserRateThrottle]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [PostThrottle, AnonRateThrottle, UserRateThrottle]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
