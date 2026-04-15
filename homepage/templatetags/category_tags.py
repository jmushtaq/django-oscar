from django import template
from oscar.apps.catalogue.models import Category, Product

register = template.Library()

@register.simple_tag
def get_top_categories():
    return Category.objects.filter(depth=1)

@register.simple_tag
def get_category_products(category, limit=3):
    """
    Get products for a specific category
    """
    products = Product.objects.filter(
        categories=category,
        is_public=True
    )[:limit]
    return products
