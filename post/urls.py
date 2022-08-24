from django.urls import path
from post.views import PostDetail, BlogView, TagDetail

urlpatterns = [

    path('', BlogView.as_view(), name='blog_page'),
    path('posts/<slug:post_slug>/', PostDetail.as_view(), name='post_single'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail'),


]

