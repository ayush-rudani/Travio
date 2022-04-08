from django import template
register = template.Library()


@register.filter(name="total_cost")
def total_cost(val1, val2):
    return val1*val2
