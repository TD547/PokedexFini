from django import template

register = template.Library()


@register.filter(name='format_id')
def format_id(value):
    value = '%d' % value
    return value.rjust(3, '0')


@register.filter(name='format_weight')
def format_weight(value):
    value = value / 10
    return value


@register.filter(name='format_height')
def format_height(value):
    value = value / 10
    return value


@register.filter(name='format_type')
def format_type(value):
    if (len(value.split(" ")) > 1):
        return value.split(" ")[0] + ", " + value.split(" ")[1]
    return value
