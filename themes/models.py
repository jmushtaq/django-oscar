from django.db import models
from django.conf import settings
from django.core.cache import cache

class Theme(models.Model):
    name = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    primary_color = models.CharField(max_length=7, default='#6366f1')
    secondary_color = models.CharField(max_length=7, default='#8b5cf6')
    accent_color = models.CharField(max_length=7, default='#ec4899')
    background_color = models.CharField(max_length=7, default='#ffffff')
    text_color = models.CharField(max_length=7, default='#1f2937')
    font_family = models.CharField(max_length=100, default="'Inter', sans-serif")
    button_style = models.CharField(max_length=20, choices=[
        ('rounded', 'Rounded'),
        ('pill', 'Pill-shaped'),
        ('square', 'Square'),
    ], default='rounded')
    card_style = models.CharField(max_length=20, choices=[
        ('shadow', 'Shadow'),
        ('border', 'Border'),
        ('flat', 'Flat'),
    ], default='shadow')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other themes
            Theme.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)
        cache.delete('active_theme')

    def __str__(self):
        return self.display_name

    @classmethod
    def get_active_theme(cls):
        cache_key = 'active_theme'
        theme = cache.get(cache_key)
        if not theme:
            try:
                theme = cls.objects.filter(is_active=True).first()
                if not theme:
                    # Create default themes if none exist
                    cls.create_default_themes()
                    theme = cls.objects.filter(is_active=True).first()
                cache.set(cache_key, theme, 3600)  # Cache for 1 hour
            except Exception:
                theme = None
        return theme

    @classmethod
    def create_default_themes(cls):
        themes_data = [
            {
                'name': 'elegant',
                'display_name': 'Elegant Gold',
                'primary_color': '#d4af37',
                'secondary_color': '#8b7355',
                'accent_color': '#c0a080',
                'background_color': '#fefcf6',
                'text_color': '#2c2418',
                'font_family': "'Playfair Display', serif",
                'button_style': 'rounded',
                'card_style': 'shadow',
                'is_active': True
            },
            {
                'name': 'modern',
                'display_name': 'Modern Minimal',
                'primary_color': '#6366f1',
                'secondary_color': '#8b5cf6',
                'accent_color': '#ec4899',
                'background_color': '#ffffff',
                'text_color': '#1f2937',
                'font_family': "'Inter', sans-serif",
                'button_style': 'rounded',
                'card_style': 'shadow',
                'is_active': False
            },
            {
                'name': 'party',
                'display_name': 'Party Bright',
                'primary_color': '#ff3366',
                'secondary_color': '#ff9933',
                'accent_color': '#33ff66',
                'background_color': '#1a1a2e',
                'text_color': '#ffffff',
                'font_family': "'Poppins', sans-serif",
                'button_style': 'pill',
                'card_style': 'border',
                'is_active': False
            },
            {
                'name': 'luxury',
                'display_name': 'Luxury Dark',
                'primary_color': '#c9a96e',
                'secondary_color': '#2c1810',
                'accent_color': '#8b4513',
                'background_color': '#0a0a0a',
                'text_color': '#e8e8e8',
                'font_family': "'Cormorant Garamond', serif",
                'button_style': 'square',
                'card_style': 'border',
                'is_active': False
            },
            {
                'name': 'floral',
                'display_name': 'Floral Fresh',
                'primary_color': '#4c9f70',
                'secondary_color': '#ffb7c5',
                'accent_color': '#e8a4c9',
                'background_color': '#fdf6f0',
                'text_color': '#2d4a3e',
                'font_family': "'Quicksand', sans-serif",
                'button_style': 'rounded',
                'card_style': 'shadow',
                'is_active': False
            }
        ]

        for theme_data in themes_data:
            cls.objects.get_or_create(
                name=theme_data['name'],
                defaults=theme_data
            )

class UserThemePreference(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='theme_preference')
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'User Theme Preference'
        verbose_name_plural = 'User Theme Preferences'
    
    def __str__(self):
        return f"{self.user.username} - {self.theme.display_name if self.theme else 'Default'}"
