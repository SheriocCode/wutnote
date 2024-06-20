"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from .views import upload_images, edit, stream_response, get_hunyuan_response

from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('note/',include('note.urls')),

    path('upload/img/',upload_images), # 上传图片
    path('edit/',edit), # 新建笔记

    path('stream_response/', stream_response, ), # 流式返回数据
    path('get_hunyuan_response/', get_hunyuan_response, name='get_hunyuan_response'),
]
