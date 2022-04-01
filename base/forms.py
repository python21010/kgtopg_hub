from django import forms
from django.forms import fields, widgets
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'body'}

    widgets = {
        # 'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'})
    }


#  from django import forms
# from .models import BlogComment

# class CommentForm(forms.ModelForm):
#     content = forms.CharField(label ="", widget = forms.Textarea(
#     attrs ={
#         'class':'form-control',
#         'placeholder':'Comment here !',
#         'rows':4,
#         'cols':50
#     }))
#     class Meta:
#         model = BlogComment
#         fields =['blog_comment_content']
