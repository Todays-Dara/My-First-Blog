from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
# Create your views here.
def post_list(request):
    me = User.objects.get(username='Darasimi')
    post = Post.objects.filter(author=me)
    return render(request,'blog/post_list.html', {"post":post})