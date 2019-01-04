"""tutorialdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# index, blog, postdetails 페이지 추가
from main.views import index, blog, postdetails

urlpatterns = [
    path('admin/', admin.site.urls),
    # url로 접속 후 첫 화면은 index.html
    path('', index),
    # localhost:80/blog 접속하면 blog 페이지
    path('blog/', blog),
    # localhost:80/blog/게시글넘버 게시글 세부페이지
    path('blog/<int:pk>/', postdetails),
]
