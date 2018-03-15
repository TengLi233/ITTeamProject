from django import template
from HotPotWebsite.models import MenuCategory

register = template.Library()

@register.inclusion_tag('HotPotWebsite/cats.html')
def get_category_list():
    return {'cats': MenuCategory.objects.all()}
