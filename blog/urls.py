from django.conf.urls import url

from . import views

app_name='blog'

urlpatterns = [
#第一个参数是网址，第二个参数是处理函数），另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #(?P<pk>[0-9]+) 表示命名捕获组，其作用是从用户访问的 URL 里把括号内匹配的字符串捕获并作为关键字参数传给其对应的视图函数 detail。
     url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    #例如如果用户想查看 2017 年 3 月下的全部文章，他访问 /archives/2017/3/，
    #那么 archives 视图函数的实际调用为：archives(request, year=2017, month=3)。
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]


#此外我们通过 app_name='blog' 告诉 Django 这个 urls.py 模块是属于 blog 应用的
