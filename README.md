# `Django`를 공부하자
현재 `Instagram`, `Pinterest`등 `django`가 기반인 프로젝트가 많습니다  
어떻게 진행하는지 궁금하다면? [장고 튜토리얼](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)  

## `Django` 환경세팅
`mysite` 폴더 만들자
```console
root@goorm:/workspace/django# mkdir mysite
```

`mysite` 폴더로 들어가자
```console
root@goorm:/workspace/django# cd mysite
```

`pip3`를 이용해 `virtualenv`를 다운로드하자  
가상환경을 설정합니다. 프로젝트 관리를 편하게 해줍니다  
자세한 내용은 검색을 해보자 이 문서는 튜토리얼이니 실습에 맞춰져 있습니다

```console
root@goorm:/workspace/django/mysite# pip3 install virtualenv
```

가상환경 설정을 위해 `virtualenv`를 `mysite/myvenv` 폴더에 설치합니다  
`/bin`, `/include`, `/lib` 폴더가 설치됩니다
```console
root@goorm:/workspace/django/mysite# virtualenv myvenv
```

설정한 가상환경을 실행합니다  
**프로젝트를 실행할때마다 반복해서 사용하는 명령어입니다**
```console
root@goorm:/workspace/django/mysite# source myvenv/bin/activate
```
django 프로젝트를 설치합니다
```console
(myvenv)root@goorm:/workspace/django/mysite# pip3 install django==2.1
```
현재 `/django/mysite` 폴더에 `/tutorialdiango` 프로젝트를 생성합니다   
`/tutorialdjango` 폴더와 `manage.py`가 생성됩니다
```console
(myvenv) root@goorm:/workspace/django/mysite# django-admin startproject tutorialdjango . 
```
`django`가 사용할 DB를 생성합니다(migrate 합니다)
```console
(myvenv) root@goorm:/workspace/django/mysite# python manage.py migrate
```
이제 `/mysite/tutorialdjango/settings.py`로 이동하셔서 28번째 줄을 수정합니다.  
모든 사용자의 접속을 허락하는 코드로 수정합니다
```python
ALLOWED_HOSTS = ['*']
```
이제 `django` 프로젝트를 실행합니다  
로컬에서 실행하는 경우 [http://0:80/](http://0:80/)로 접속합니다  
구름 IDE를 사용하는 경우 `/프로젝트/실행 URL과 포트`에서 80번 포트를 설정 후 접속합니다
```console
(myvenv) root@goorm:/workspace/django/mysite# python manage.py runserver 0:80 
```
아래의 그림이 뜨면 `django` 설치 완료  
![django_install_complete_window](/img/django_install_complete.png)

## 첫 페이지 만들자

`/mysite` 폴더 아래에 `/main`폴더를 만듭니다
```console
(myvenv) root@goorm:/workspace/django/mysite# python manage.py startapp main
```
`/mysite/tutorialdjango/settings.py`의 33번째 줄을 보면 `INSTALLED_APPS`가 있습니다

수정을 안한 `django` 기본 세팅값은 아래와 같습니다
##### 수정 전 `settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
좀 전에 수정한 `main` app을 추가합시다.   
이 작업을 하지 않으면 앱이 구동하지 않습니다.  
여러 개의 앱을 만들 경우 모두 여기 등록합니다.  

##### 수정 후 `settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]
```
이제 `/mysite/tutorialdjango/urls.py`파일을 수정합니다  
사용자가 어떤 url을 사용해 들어오는지를 확인해봅시다  
여기선 사용자가 url로 접속시 첫 화면을 설정합니다  

##### 수정 전 `urls.py`
```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

##### 수정 후 `urls.py`
```python
from django.contrib import admin
from django.urls import path
from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # url로 접속 후 첫 화면은 index
    path('',index),
]
```

`/mysite/main/views.py`에서 index 함수를 만듭니다.  
사용자가 `index.html'`을 볼 수 있게 연결합니다.  

##### `views.py`
```python
from django.shortcuts import render

# index.html로 연결해주는 index 함수
def index(request):
    return render(request, 'main/index.html')
```
`/mysite/main/templates/main/index.html` 경로로 `index.html`파일을 만듭니다  
아래의 마크업을 `index.html`파일에 넣습니다
```html
<html>
<head>
    <title>Django Tutorial</title>
</head>
<body>
    <h1>메인 페이지입니다</h1>
</body>
</html>
```
서버를 키고 확인합시다
```console
(myvenv) root@goorm:/workspace/django/mysite# python manage.py runserver 0:80 
```
아래의 화면이 나오면 성공!  
![/img/mainPageTest.png](/img/mainPageTest.png)

#### 관리자 `admin` 접속
`https://웹페이지URL/admin` url로 들어갑니다  
아래의 화면이 나오면 성공!  
![/img/djangoAdmin.png](/img/djangoAdmin.png)

#### 정적 이미지 불러오자

`/mysite/static` 폴더를 만들고, 원하는 이미지 파일을 넣습니다.  
그 후 `/static` 폴더와 `django`와 연결시킵니다.  
[Static 파일 호출하기 django 공식문서](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#static)
##### 수정 전 `settings.py`
121번째 줄
```python
STATIC_URL = '/static/'
```
##### 수정 후 `settings.py`
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # django와 static 폴더 연결
    os.path.join(BASE_DIR, 'static'),
)
```

##### 수정 후 `index.html` 
```html
<html>
<head>
    <title>Django Tutorial</title>
</head>
<body>
    <h1>메인 페이지입니다</h1>
    <!-- 정적 이미지 불러오기 -->
    {% load staticfiles %}
    <img src="{% static 'digital-nomad-gear.jpg' %}">
</body>
</html>
```
![img/static_img.png](img/static_img.png)

#### Time Zone 변경
한국 시간대로 맞춰줍니다
##### 수정 후 `settings.py`
109번째 줄
```python
TIME_ZONE = 'Asia/Seoul'
```
#### `Django`의 구조
`Django`는 `MVC`모델을 `MTV`라고 부릅니다  
자세한건 다음에 또 다루겠습니다  

`CRUD`는 대부분의 컴퓨터 소프트웨거 가지는 기본적인 데이터 처리 기능인  
Create(생성), Read(읽기), Update(갱신), Delete(삭제)를 묶어서 일컫는 말입니다.  


|  이름  | 조작 |   SQL  |
|:------:|:----:|:------:|
| Create | 생성 | INSERT |
|  Read  | 읽기 | SELECT |
| Update | 갱신 | UPDATE |
| Delete | 삭제 | DELETE |


## `Blog` 페이지 만들자

##### 수정 후 `urls.py`
```python
from django.contrib import admin
from django.urls import path
# index, blog 페이지 추가
from main.views import index, blog

urlpatterns = [
    path('admin/', admin.site.urls),
    # url로 접속 후 첫 화면은 index.html
    path('', index),
    # localhost:80/blog 접속하면 blog 페이지
    path('blog/', blog),
]
```

##### 수정 후 `views.py`
```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    return render(request, 'main/blog.html')
```

###### `mysite/main/template/main/blog.html` 작성
```html
<html>
<head>
    <title>Django Tutorial!</title>
</head>
<body>
    <h1>Blog Page!</h1>
</body>
</html>
```
![블로그 페이지 띄우기](img/Blog_page.png)  
위의 페이지가 뜨면 성공!  


서버를 어떻게 실행했는지 기억나시나요?
### `웹서버 실행` 복습  

**프로젝트를 실행할때마다 반복해서 사용하는 명령어입니다**  
파이썬 가상환경 설정 
```console
root@goorm:/workspace/django/mysite# source myvenv/bin/activate
```
이제 `django` 웹서버를 실행합시다  
로컬에서 실행하는 경우 [http://0:80/](http://0:80/)로 접속합니다  
구름 IDE를 사용하는 경우 `/프로젝트/실행 URL과 포트`에서 80번 포트를 설정 후 접속합니다
```console
(myvenv) root@goorm:/workspace/django/mysite# python manage.py runserver 0:80 
```

### `Model` 만들기

블로그에서 각각의 포스팅에 저장될 공간을 만듭니다.  
`Post` 게시글 마다 `postname`(제목), `contents`(내용)이 존재합니다.  
이를 구현한 아래의 파이썬 코드

##### `mysite/main/models.py`
```python
from django.db import models

class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
```

이제 모델을 만들었고 `django`의 db에 `migrate`해줍니다  
게시글마다 제목과 내용을 저장할 수 있게 됩니다  

##### `Ctrl + C`를 눌러 `웹서버`를 종료 후 `migration`

```console
(myvenv) root@goorm:/workspace/django/mysite# python manage.py makemigrations main
```

```console
(myvenv) root@goorm:/workspace/django/mysite# python manage.py migrate
```
![post migration](img/post_migration.png)  

#### `Admin`에 권한
##### `mysite/main/admin.py`
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
#### `Superuser` 만들기
`Superuser`는 게시글 삭제, 수정, 저장하고,  
다른 유저들을 관리합니다.
```console
(myvenv) root@goorm:/workspace/django/mysite# python manage.py createsuperuser
```
![createsuperuser](img/createsuperuser.png)  
간단한 비밀번호를 입력하니 똑똑한 장고가 거부합니다  
이제 `Admin User`를 만들었고 [http://0:80/admin](http://0:80/admin)으로 접속합니다  
`Admin User`의 아이디와 비밀번호를 입력해 관리자 페이지로 들어갑니다  
![django_administration](img/django_administration.png)  
위의 페이지가 나오면 성공!
```python
```
```python
```
```python
```
