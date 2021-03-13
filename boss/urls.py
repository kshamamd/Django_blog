from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView,\
      PostDeleteView, task_com
from . import views

urlpatterns = [
      path('', PostListView.as_view(), name='boss-home'),
      path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
      path('post/new/', PostCreateView.as_view(), name='post-create'),
      path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
      path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
      #path('post/<int:pk>', PostLikedRedirect.as_view(), name='post-likes'),
      #path('like/<int:pk>', LikeView.as_view(), name='like_post'),
      #path('', views.home, name='boss-home'),
      path('search', views.search, name='search'),
      path('task_com', views.task_com, name='task_com'),

    ]


