# `Django`를 공부하자
현재 `Youtube`, `Instagram`등 `django`가 기반인 프로젝트가 많습니다  
어떻게 진행하는지 궁금하다면? [장고 튜토리얼](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)  

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
