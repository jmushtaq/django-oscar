from .models import Theme

def active_theme(request):
    try:
        return {
            'active_theme': Theme.get_active_theme()
        }
    except Exception:
        # Return a default theme if there's an error
        return {
            'active_theme': None
        }
