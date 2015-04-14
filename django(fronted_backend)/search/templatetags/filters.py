#coding: utf-8 

from django import template
from irkonline.search.models import Seller

register = template.Library()

@register.filter(name='seller')
def seller(ids):
    try:
        s = Seller.objects.filter(id=int(ids))
        return s[0].name
    except Exception:
        return ''  

@register.filter(name='slice_url')
def sliceurl(url_prod):
    try:
        return url_prod[:35]
    except Exception:
        return ''