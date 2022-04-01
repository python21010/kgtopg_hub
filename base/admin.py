# from base.models import Post
from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)


# from django.contrib import admin
# from .models import User, Blog,BlogCat,BlogComment,BlogDislike,BlogLike
# from django.template.defaulttags import register

# # Register your models here.
# admin.site.register(User)
# admin.site.register(Blog)
# admin.site.register(BlogCat)
# admin.site.register(BlogComment)
# admin.site.register(BlogDislike)
# admin.site.register(BlogLike)


# @register.filter
# def get_item(post, key):
#     return post.get(key)
