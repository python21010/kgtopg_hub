from requests.sessions import Request
from base.models import LikesModel, DisLikesModel
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from .models import Category, Comment, Post
from .forms import CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
import jwt
from django.conf import settings
# Create your views here.


# import requests

# url = ('https://newsapi.org/v2/everything?'
#        'q=Apple&'
#        'from=2021-09-02&'
#        'sortBy=popularity&'
#        'apiKey=ad39711598e5490d8b56228cfd8d77d9')

# response = requests.get(url)


def home(request):
    token = request.GET.get('token')
    referer = request.GET.get('referer', settings.SITE_URL)
    logo = request.GET.get('logo', '')
    if token:
        secret_key = 'g=#$a&)xi74w3d7w_z+ipzy&f1%inc(ji2%f(e0u9li&xto)bb'
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        print(payload, "7777777777777777777777777777777777777777777777777777")
        email = payload['sub']
        pwd = payload['pwd']
        print(email, "+++++++++++++++++++++++++++++++++++++++++++++")
        print(pwd, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22")
        dict_data = {
            "token": token
        }
        # dict_data={
        # 	"token":email
        # }
        import requests

        # url = ('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ad39711598e5490d8b56228cfd8d77d9')
        url = ('https://newsapi.org/v2/everything?q=education&sortBy=popularity&apiKey=ad39711598e5490d8b56228cfd8d77d9')
        response = requests.get(url)
        resp = response.json()
        article = resp['articles']

        # print(article, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        # import feedparser

        # NewsFeed = feedparser.parse(
        #     "https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

        # print('Number of RSS posts :', len(NewsFeed.entries))
        # for i in range(15):
        #     entry = NewsFeed.entries[i]
        #     print('Post Title :', entry.title)
        #     print('Post content :', entry.description)
        #     # print('Post entry :', entry.image)
        # entry = NewsFeed.entries
        # print(response.json())
        import json
        import requests
        json_data = json.dumps(dict_data)
        try:
            json_data = requests.get(
                f"{settings.PLATFORM_URL}/user-details/", data=json_data)
        except:
            return HttpResponse("<html><body><center><h1>Service is not available</h1></center></body></html>")
        else:
            python_dict = dict(json_data.json())
            request.session["email"] = python_dict['user_email']
            request.session["user_id"] = python_dict['user_id']
            context_obj = {
                'posts': Post.objects.all(),
                "user_data": python_dict,
                # 'entry': entry,
                'article': article,
                'email': email,
                'pwd': pwd,
                "token": token,
                'PUSTAK_URL': settings.PUSTAK_URL,
                'SCHOOLER_URL': settings.SCHOOLER_URL,
                'SITE_URL': settings.SITE_URL,
                'QBANK_URL': settings.QBANK_URL
            }

            return render(request, 'base/index1.html', context_obj)

    context_obj = {
        'posts': Post.objects.all(),
        "user_data": None,
        'email': None,
        'pwd': None,
        'PUSTAK_URL': settings.PUSTAK_URL,
        'SCHOOLER_URL': settings.SCHOOLER_URL,
        'SITE_URL': settings.SITE_URL,
        'QBANK_URL': settings.QBANK_URL
    }
    return redirect(f"{settings.AUTH_URL}/login?referer={referer}&logo={logo}")


def user_logout(req):
    uid = req.POST.get("uid")
    u_role_id = req.POST.get("u_role_id")
    u_mail = req.POST.get("u_mail")
    x = 0
    try:
        # del req.session["email"]
        # del req.session["user_id"]
        x = 2
    except:
        return HttpResponse("Session Not Found")
    else:
        return redirect(f"{settings.AUTH_URL}/logout")


# class PostListView(ListView):
#     model = Post
#     template_name = 'base/index.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']


class CategoryListView(View):
    def get(self, req):
        id = req.GET.get("id")
        model = Post.objects.filter(category=id)
        template_name = 'base/cat_list.html'
        return render(req, template_name, {"model": model})


class PostDetailView(View):
    def get(self, req, pk):
        qs = Post.objects.get(id=pk)
        form_class = CommentForm
        posts = Post.objects.all()
        print(qs.category, "categery nasme")
        category = Category.objects.all()
        posts2 = Post.objects.filter(category=qs.category)

        # def form_valid(self, form):
        #     form.instance.post_id = self.kwargs['pk']
        #     return super().form_valid(form)
        # # success_url = reverse_lazy('blog-home')
        return render(req, "base/post_detail.html", {'post': qs, "form": form_class, 'posts': posts, 'category': category, "posts2": posts2})
    # model = Post
    # template_name = 'blog/post_detail.html'


def savec(req):
    # name = req.POST.get("name")
    # print(req.POST, 'asydgyuawgdyuagfyjgfyegbhyjgfyeb')
    body = req.POST.get("body")
    id = req.POST.get("id")
    user_id = req.session["user_id"]
    print(user_id, "user_________________________iddddddddddddddddd")
    user_name = req.session["email"]
    # print(user_name, "user_______________-nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

    Comment.objects.create(post_id=id,  body=body,
                           user_id=user_id, name=user_name)
    ps = PostDetailView()
    urlpa = '/post/'+str(id)+'/'
    return redirect(urlpa)


def LikeView(request):
    id = request.POST.get("id")
    user_id = request.session["user_id"]
    qs = Post.objects.get(id=id)
    category = Category.objects.all()
    posts2 = Post.objects.filter(category=qs.category)
    form_class = CommentForm
    posts = Post.objects.all()
    data = LikesModel.objects.filter(user_id=user_id)
    t2 = DisLikesModel.objects.filter(user_id=user_id)
    DisLikesModel.objects.filter(user_id=user_id).delete()
    dis = []
    if t2:
        for x in t2:
            dis.append(x.dislikecount)
    else:
        dis.append(0)

    if data:
        try:
            ob = LikesModel.objects.get(user_id=user_id)
        except:
            print("No data available")
    else:
        LikesModel.objects.create(
            likecount=1, blog_id=id, user_id=user_id)
        try:
            ob = LikesModel.objects.get(user_id=user_id)

        except:
            print("No data available")

    return render(request, "base/post_detail.html", {'post': qs, "form": form_class, 'posts': posts, 'category': category, "posts2": posts2, "total_likes": ob.likecount, "total_dislikes": dis[0]})


# def LikeView(request):
#     id = request.POST.get("id")
#     qs2 = LikesModel.objects.filter(blog_id=id)
#     qs = Post.objects.get(id=id)
#     form_class = CommentForm
#     posts = Post.objects.all()
#     print(qs.category, "categery nasme")
#     category = Category.objects.all()
#     posts2 = Post.objects.filter(category=qs.category)
#     t2 = DisLikesModel.objects.filter(blog_id=id)
#     t_value = []
#     if t2:
#         for x in t2:
#             t_value.append(x.dislikecount)
#     else:
#         t_value.append(0)
#     if qs2:
#         like_c = []
#         qsd = LikesModel.objects.filter(blog_id=id)
#         for x in qsd:
#             like_c.append(x.likecount)
#         likes = int(like_c[0])+1
#         qsd.update(likecount=likes, blog_id=id)
#         t = LikesModel.objects.get(blog_id=id, user_id=id)
#         return render(request, "base/post_detail.html", {'post': qs, "form": form_class, 'posts': posts, 'category': category, "posts2": posts2, "total_likes": str(t.likecount), "total_dislikes": str(t_value[0])})

#     else:
#         user_id = request.session["user_id"]

#         lik = LikesModel.objects.get(blog_id=id, user_id=user_id)
#         if not lik:

#             LikesModel.objects.create(likecount=1, blog_id=id, user_id=user_id)
#         t = LikesModel.objects.get(blog_id=id)
#         return render(request, "base/post_detail.html", {'post': qs, "form": form_class, 'posts': posts, 'category': category, "posts2": posts2, "total_likes": str(t.likecount), "total_dislikes": str(t_value[0])})


# # def DoLikeView(request):
# #     try:
# #         user_id = request.session["user_id"]
# #         lik = LikesModel.objects.get(blog_id=id, user_id=user_id)
# #         if not lik:
# #             LikesModel.objects.create(likecount=1, blog_id=id, user_id=user_id)


def DisLikeView(request):
    id = request.POST.get("id")
    user_id = request.session["user_id"]
    qs = Post.objects.get(id=id)
    category = Category.objects.all()
    posts2 = Post.objects.filter(category=qs.category)
    form_class = CommentForm
    posts = Post.objects.all()
    t2 = LikesModel.objects.filter(user_id=user_id)
    data = DisLikesModel.objects.filter(user_id=user_id)
    LikesModel.objects.filter(user_id=user_id).delete()
    dis = []
    if t2:
        for x in t2:
            dis.append(x.likecount)
    else:
        dis.append(0)

    if data:
        try:
            ob = DisLikesModel.objects.get(user_id=user_id)
        except:
            print("No data available")
    else:
        DisLikesModel.objects.create(
            dislikecount=1, blog_id=id, user_id=user_id)
        try:
            ob = DisLikesModel.objects.get(user_id=user_id)

        except:
            print("No data available")

    return render(request, "base/post_detail.html", {'post': qs, "form": form_class, 'posts': posts, 'category': category, "posts2": posts2, "total_likes": dis[0], "total_dislikes": ob.dislikecount})


# def DisLikeView(request):
#     id = request.POST.get("id")
#     qs2 = DisLikesModel.objects.filter(blog_id=id)
#     qs = Post.objects.get(id=id)
#     form_class = CommentForm
#     posts = Post.objects.all()
#     print(qs.category, "categery nasme")
#     category = Category.objects.all()
#     posts2 = Post.objects.filter(category=qs.category)
#     t2 = LikesModel.objects.filter(blog_id=id)
#     t_value = []
#     if t2:
#         for x in t2:
#             t_value.append(x.likecount)
#     else:
#         t_value.append(0)
#     if qs2:
#         dislike_c = []
#         qsd = DisLikesModel.objects.filter(blog_id=id)
#         for x in qsd:
#             dislike_c.append(x.dislikecount)
#         likes = int(dislike_c[0])+1
#         qsd.update(dislikecount=likes, blog_id=id)
#         t = DisLikesModel.objects.get(blog_id=id)

#         return render(request, "base/post_detail.html", {'post': qs, "form": form_class, 'posts': posts, 'category': category, "posts2": posts2, "total_dislikes": str(t.dislikecount), "total_likes": str(t_value[0])})

#     else:
#         user_id = request.session["user_id"]

#         DisLikesModel.objects.create(
#             dislikecount=1, blog_id=id, user_id=user_id)
#         t = DisLikesModel.objects.get(blog_id=id)
#         return render(request, "base/post_detail.html", {'post': qs, "form": form_class, 'posts': posts, 'category': category, "posts2": posts2, "total_dislikes": str(t.dislikecount), "total_likes": str(t_value[0])})


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "base/add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('blog-home')


# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# import jwt
# from django.core.exceptions import PermissionDenied
# from .models import User
# from .models import Blog, BlogComment, BlogCat
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .forms import CommentForm


# # Create your views here.
# def set_password_md5(raw_password):
#     hash_obj = hashlib.sha1((raw_password).encode('utf8'))
#     password = hash_obj.hexdigest()
#     return password


# def index(request):

#     token = None
#     posts = None

#     try:
#         posts = Blog.objects.values()
#         # posts2=BlogCat.objects.all()
#         if posts:
#             for post in posts:
#                 cat = BlogCat.objects.filter(
#                     blog_cat_id=post['blog_cat_id']).values()

#                 post.update({'cat': cat[0]})
#                 print("post is update", post)
#             # 	post_list.append(cat.blog_cat_title)
#             # 	post_list_id.append(cat.blog_cat_id)
#             # print(post_list,"+++++++++++++++++++++++")
#         token = request.GET['token']

#         # authenticate the token
#         if token:
#             secret_key = 'g=#$a&)xi74w3d7w_z+ipzy&f1%inc(ji2%f(e0u9li&xto)bb'
#             payload = jwt.decode(token, secret_key, algorithms=["HS256"])
#             email = payload['sub']

#             user = User.objects.get(user_email=email)

#             if user:
#                 print('User authenticated and can proceed')
#             else:
#                 print('User not authenticated.. Redirect him back.. to about.kgtopg.com')
#             template = 'base/index.html'
#         else:
#             raise PermissionDenied

#     except Exception as e:
#         token = None
#         # posts = None
#         print('warning - exception reading token %s' % e)
#         # raise PermissionDenied
#         template = 'base/index.html'

#     context = {
#         # 'post_list':post_list,
#         # 'post_list_id':post_list_id,
#         'posts': posts,
#         'token': token
#     }
#     # return HttpResponse('Welcome to KGtoPG hub!')
#     return render(request, 'base/index.html', context)


# # class Postdetail(DetailView):
# # 	model = Blog


# def blog_detail(request, id):
#     post = get_object_or_404(Blog, blog_id=id)

# 	comments = post.

#     comments = BlogComment.objects.filter(blog_id=post['blog_id']).values()

#     if request.method == 'POST':

#         cf = CommentForm(request.POST or None)
#         if cf.is_valid():
#             new_comment = cf.save(commit=False)
#             new_comment.post = post
#             new_comment.save()

#     else:
#         cf = CommentForm()

#         # content = request.POST.get('blog_comment_content')
#         # comment = BlogComment.objects.create(
#         #     post=post, user=request.user, content=content)
#         # comment.save()
#         # return redirect(post.get_absolute_url())
#         # else:
#         #     cf = CommentForm()

#     context = {
#         'post': post,
#         'comments': comments,
#         'new_comment': new_comment,
#         'comment_form': cf
#     }
#     return render(request, 'base/blogdetail.html', context)
def profile(request):
    return render(request, 'base/profile.html')


def books(request):
    return render(request, 'base/books.html')


def finance(request):
    return render(request, 'base/finance.html')


def analytics(request):
    return render(request, 'base/analytics.html')


def setting(request):
    return render(request, 'base/setting.html')
