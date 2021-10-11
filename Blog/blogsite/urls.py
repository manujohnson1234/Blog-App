from django.urls import path

from .views import HomeView, DetailHome, CreatePost, UpdatePost, DeletePost, AddCategoryView, categoryView, likeView

urlpatterns = [
    path('', HomeView.as_view(), name='blogs'),
    path('detail/<int:pk>', DetailHome.as_view(), name='blog'),
    path('add_post/', CreatePost.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('update-post/<int:pk>', UpdatePost.as_view(), name='update-post'),
    path('delete-post/<int:pk>', DeletePost.as_view(), name='delete-post'),
    path('categories/<str:cats>', categoryView, name='categories'),
    path('like_post/<int:pk>', likeView, name='like_post'),
]
