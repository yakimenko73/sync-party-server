from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware


class CookielessSessionMiddleware(SessionMiddleware):
    def process_response(self, request, response):
        response = super(CookielessSessionMiddleware, self).process_response(request, response)
        response.cookies.pop(settings.SESSION_COOKIE_NAME, None)
        return response

    def process_request(self, request):
        session_key = request.headers.get(settings.SESSION_HEADER_NAME)
        request.session = self.SessionStore(session_key)
