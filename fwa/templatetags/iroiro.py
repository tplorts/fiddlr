from django import template
from django.utils.safestring import mark_safe
from django.core.serializers.json import DjangoJSONEncoder
import re
import json


register = template.Library()


@register.filter
def split(string, delimiter):
    return string.split(delimiter)


@register.filter
def toJSON(something):
    return mark_safe(json.dumps(something, cls=DjangoJSONEncoder))


@register.filter
def space2newline(text):
    o = re.sub(r'\s+', r'<br>', text)
    return mark_safe(o)


@register.inclusion_tag('tags/placeholder-copy.html')
def placeholder_copy(*args, **kwargs):
    if 'length' not in kwargs:
        kwargs['length'] = 2
    return kwargs


@register.inclusion_tag('tags/octagram-loader.html')
def OctagramLoader( *args, **kwargs ):
    return kwargs
