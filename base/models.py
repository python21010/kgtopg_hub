from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=512, default=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    dislikes = models.ManyToManyField(User, related_name='blog_posts1')
    category = models.ForeignKey(
        Category, default=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()


class Comment(models.Model):
    user_id = models.IntegerField(default=0)
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


class LikesModel(models.Model):
    user_id = models.IntegerField(default=0)

    like_id = models.AutoField(primary_key=True)
    likecount = models.IntegerField()
    blog_id = models.IntegerField()


class DisLikesModel(models.Model):
    user_id = models.IntegerField(default=0)

    dislike_id = models.AutoField(primary_key=True)
    dislikecount = models.IntegerField()
    blog_id = models.IntegerField()


# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
# # from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# # from .managers import UserManager


# # class AdminRole(models.Model):
# #     user_role_name = models.CharField(max_length=30,unique=True)
# #     user_role_f_desc = models.CharField(max_length=255)
# #     created_date = models.DateField()
# #     timestamp = models.DateTimeField()

# #     class Meta:
# #         verbose_name='Admin Role'
# #         db_table = 'users_role'

# #     def __str__(self):
# #         return self.user_role_name

# # class AdminUsers(AbstractBaseUser,PermissionsMixin):
# #     # email = models.EmailField(max_length=254, unique=True)
# #     # roles = models.CharField(max_length=100,blank =True)
# #     admin_role_id = models.ForeignKey(AdminRole,to_field='user_role_name',on_delete=models.SET_NULL,null=True,verbose_name='Role',blank=True)
# #     # admin_role_id = models.ManyToManyField(AdminRoles)
# #     email = models.ForeignKey(User,to_field='user_email',on_delete=models.SET_NULL,null =True,unique=True)
# #     is_staff = models.BooleanField(default=False)
# #     is_active = models.BooleanField(default=True)
# #     date_joined = models.DateTimeField(default=timezone.now)

# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = []

# #     objects = UserManager()

# #     class Meta:
# #         unique_together = ('email', 'admin_role_id',)
# #         verbose_name = u'Admin'

# #     def __str__(self):
# #         return self.email.user_email


# # class AdminRole(models.Model):
# #     user_role_name = models.CharField(max_length=30,unique=True)
# #     user_role_f_desc = models.CharField(max_length=255)
# #     created_date = models.DateField()
# #     timestamp = models.DateTimeField()

# #     class Meta:
# #         verbose_name='Admin Role'
# #         db_table = 'users_role'

# #     def __str__(self):
# #         return self.user_role_name

# class Blog(models.Model):
#     blog_id = models.AutoField(primary_key=True)
#     blog_cat_id = models.PositiveIntegerField()
#     login_type_id = models.PositiveIntegerField()
#     blog_title = models.CharField(max_length=255)
#     blog_content = models.TextField()
#     blog_image_url = models.CharField(max_length=512)
#     blog_status = models.IntegerField()
#     blog_gender = models.IntegerField()
#     blog_age_max = models.PositiveIntegerField()
#     created_date = models.DateField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'blog'


# class BlogCat(models.Model):
#     blog_cat_id = models.AutoField(primary_key=True)
#     blog_cat_title = models.CharField(max_length=255)
#     blog_cat_f_desc = models.CharField(max_length=512)
#     blog_cat_status = models.IntegerField()
#     created_date = models.DateField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'blog_cat'


# class BlogComment(models.Model):
#     blog_comment_id = models.AutoField(primary_key=True)
#     blog_id = models.PositiveIntegerField()
#     user_id = models.PositiveIntegerField()
#     blog_comment_content = models.TextField()
#     blog_comment_status = models.IntegerField()
#     created_date = models.DateField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'blog_comment'


# class BlogDislike(models.Model):
#     blog_dislike_id = models.AutoField(primary_key=True)
#     blog_id = models.PositiveIntegerField()
#     user_id = models.PositiveIntegerField()
#     created_date = models.DateField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'blog_dislike'


# class BlogLike(models.Model):
#     blog_like_id = models.AutoField(primary_key=True)
#     blog_id = models.PositiveIntegerField()
#     user_id = models.PositiveIntegerField()
#     created_date = models.DateField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'blog_like'

# # Create your models here.


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_role_id = models.PositiveIntegerField()
#     user_full_name = models.CharField(max_length=70)
#     user_email = models.CharField(max_length=70)
#     user_password = models.CharField(max_length=50)
#     user_jwt_token = models.TextField()
#     user_phone = models.CharField(max_length=20)
#     user_dob = models.DateField()
#     user_gender = models.CharField(max_length=1)
#     user_photo = models.CharField(max_length=200)
#     user_reg_date = models.DateTimeField()
#     user_auth_token = models.CharField(max_length=512)
#     user_status = models.IntegerField()
#     created_date = models.DateField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'user'
