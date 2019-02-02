from django import template
from ..models import Post, Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    #接受的三个参数值表明了这些含义，一个是 created_time ，即 Post 的创建时间，
    #month 是精度，order='DESC' 表明降序排列（即离当前越近的时间越排在前面）
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()
