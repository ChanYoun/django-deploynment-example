"""learning_templates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Class-based views old version...
    1. Add an import: from other_app.views import home
        ex]from django.conf.urls import url
    2. Add a URL to urlpatterns: url(r'^$', Home.as_view(), name='home')
        ex] urlpatterns = [
                    url(r'^$',views.index, name='index'),
        ]
        ###r'^$'은 홈페이지 [localhost:8000 or 127.0.0.1:8000]을 의미한다.
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
#from django.contrib import url,include
from basic_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('basic_app/', include('basic_app.urls')), #goto basic_app\urls.py의 relative views, 즉 relative_url_templates.html
]