from oscar.apps.basket.middleware import BasketMiddleware
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class CustomBasketMiddleware(BasketMiddleware):
    def apply_offers_to_basket(self, request, basket):
        # Skip applying offers entirely
        pass


class ForceEnglishMiddleware(MiddlewareMixin):
    """Force all requests to use English (British) regardless of URL prefix"""

    def process_request(self, request):
        # Always activate English
        translation.activate('en-gb')
        request.LANGUAGE_CODE = 'en-gb'
        # Set session and cookie
        request.session['django_language'] = 'en-gb'

