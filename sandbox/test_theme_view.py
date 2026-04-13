from django.shortcuts import render
from themes.models import Theme

def test_theme(request):
    context = {
        'active_theme': Theme.get_active_theme()
    }
    return render(request, 'debug_theme.html', context)
