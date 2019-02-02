from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    #如果表单对应有一个数据库模型（例如这里的评论表单对应着评论模型），
    #那么使用 ModelForm 类会简单很多，这是 Django 为我们提供的方便。
    class Meta:
        model = Comment  #model = Comment表明这个表单对应的数据库模型是 Comment 类。
        fields = ['name', 'email', 'url', 'text']  #指定了表单需要显示的字段
