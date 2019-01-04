from django.shortcuts import render
# 모델에 Post 가져오기
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

# blog에 Post를 전부 가져오자
def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist':postlist})

# 게시글별 세부페이지
def postdetails(request, pk):
    postlist = Post.objects.get(pk=pk)
    return render(request, 'main/postdetails.html', {'postlist':postlist})