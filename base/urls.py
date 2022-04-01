from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('', views.home, name='blog-home'),
    # path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add-comment'),
    path('like/', LikeView, name='like-post'),
    path('Dislike/', DisLikeView, name='dislike-post'),
    path('category/', CategoryListView.as_view(), name='cat_list'),
    path('save_c/', savec),
    path('user-logout/', user_logout, name='user-logout'),
    path('profile/', profile, name='profile'),
    path('books/', books, name='books'),
    path('analytics/', analytics, name='analytics'),
    path('finance/', finance, name='finance'),



    # path('about/', views.about, name='blog-about'),

]


# from django.urls import path
# # from .views import PostDetailView
# from . import views

# app_name = 'kgtopg_hub'
# urlpatterns = [
#     path('', views.index, name="index"),
#     # path('post/<int:pk>/', PostDetailView.as_view(), name='blogdetail'),
#     path('blog_detail/<int:id>', views.blog_detail, name="blog_detail")
# ]
