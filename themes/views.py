from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Theme

@staff_member_required
def theme_selector(request):
    themes = Theme.objects.all()
    active_theme = Theme.get_active_theme()

    if request.method == 'POST':
        theme_id = request.POST.get('theme')
        if theme_id:
            try:
                theme = Theme.objects.get(id=theme_id)
                # Deactivate all themes
                Theme.objects.filter(is_active=True).update(is_active=False)
                # Activate selected theme
                theme.is_active = True
                theme.save()
                messages.success(request, f'✨ Theme changed to {theme.display_name}! Refresh the page to see the changes.')
            except Theme.DoesNotExist:
                messages.error(request, 'Theme not found')
        return redirect('themes:theme-selector')

    return render(request, 'themes/theme_selector.html', {
        'themes': themes,
        'active_theme': active_theme,
    })

def preview_theme(request, theme_id):
    """Preview a theme without activating it"""
    theme = get_object_or_404(Theme, id=theme_id)
    return render(request, 'themes/theme_preview.html', {
        'preview_theme': theme,
        'themes': Theme.objects.all(),
    })
