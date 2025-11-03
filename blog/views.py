from django.shortcuts import render
from .models import Post
from django.utils import timezone

# 添加这个视图函数
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# from django.shortcuts import render
# from django.utils import timezone
# from .models import Post

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {})