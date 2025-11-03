from django.shortcuts import render

# 添加这个视图函数
def post_list(request):
    return render(request, 'blog/post_list.html', {})
