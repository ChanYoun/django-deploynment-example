from django.conf.urls import url
from basic_app import views

#Template Tagging
app_name = 'basic_app'
     #match relative_url_templates.html <a href...></> url name
urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
