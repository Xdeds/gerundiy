"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from school.views import main, gallery, table1, teacher, student, graduate, priem, table2

urlpatterns = [
    path('', main, name='main'),
    path('gallery/', gallery, name='gallery'),
    path('teacher/', teacher, name='teacher'),
    path('student/', student, name='student'),
    path('graduate/', graduate, name='graduate'),
    path('table1/', table1, name='table1'),
    path('table2/', table2, name='table2'),
    path('priem/', priem, name='priem'),
]
