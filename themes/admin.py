from django.contrib import admin
from .models import Theme, UserThemePreference

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['display_name', 'name']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'display_name', 'is_active')
        }),
        ('Colors', {
            'fields': ('primary_color', 'secondary_color', 'accent_color', 'background_color', 'text_color')
        }),
        ('Typography & Style', {
            'fields': ('font_family', 'button_style', 'card_style')
        }),
    )

@admin.register(UserThemePreference)
class UserThemePreferenceAdmin(admin.ModelAdmin):
    list_display = ['user', 'theme', 'updated_at']
    list_filter = ['theme']
    search_fields = ['user__username', 'user__email']
