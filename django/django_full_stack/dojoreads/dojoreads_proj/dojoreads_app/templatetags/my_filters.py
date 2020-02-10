from django import template

register = template.Library()


@register.filter()
def star_range(min=5):
    return range(min)
