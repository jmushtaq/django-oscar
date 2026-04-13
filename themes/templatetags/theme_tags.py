from django import template
from django.utils.safestring import mark_safe
from django.core.cache import cache
from themes.models import Theme

register = template.Library()

@register.simple_tag
def get_active_theme():
    try:
        return Theme.get_active_theme()
    except:
        return None

@register.simple_tag
def theme_css_variables():
    try:
        theme = Theme.get_active_theme()
        if theme:
            return mark_safe(f"""
            <style>
                :root {{
                    --primary-color: {theme.primary_color};
                    --secondary-color: {theme.secondary_color};
                    --accent-color: {theme.accent_color};
                    --background-color: {theme.background_color};
                    --text-color: {theme.text_color};
                    --font-family: {theme.font_family};
                    --button-style: {theme.button_style};
                    --card-style: {theme.card_style};
                }}

                /* Global styles using CSS variables */
                body {{
                    background-color: var(--background-color);
                    color: var(--text-color);
                    font-family: var(--font-family);
                }}

                .btn-primary {{
                    background-color: var(--primary-color);
                    border-color: var(--primary-color);
                }}

                .btn-primary:hover {{
                    background-color: var(--primary-color);
                    filter: brightness(90%);
                }}

                .btn-secondary {{
                    background-color: var(--secondary-color);
                    border-color: var(--secondary-color);
                }}

                .product-card {{
                    border-radius: 8px;
                    overflow: hidden;
                }}

                .product-card:hover {{
                    transform: translateY(-5px);
                    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                }}
            </style>
            """)
    except:
        return mark_safe("<style>:root{--primary-color:#6366f1;}</style>")
    return ""

@register.filter
def theme_color(color):
    """Filter to apply theme colors to elements"""
    return color
