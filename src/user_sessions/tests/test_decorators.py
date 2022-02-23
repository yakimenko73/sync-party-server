from django.contrib.sessions.backends.cache import SessionStore
from django.test import SimpleTestCase

from user_sessions.decorators import *


class RequestMock:
    session = SessionStore()


class TestDecorators(SimpleTestCase):
    def setUp(self):
        self.request = RequestMock()

    def test_saving_session_decorator(self):
        handle_unsaved_session(lambda _, __: None)(None, self.request)
        self.assertIsNotNone(self.request.session.session_key)

    def test_setting_session_data_decorator(self):
        import cache
        set_random_session_data(lambda _, __: None)(None, self.request)
        try:
            self.assertIsNotNone(self.request.session['nickname'])
            self.assertIsNotNone(self.request.session['color'])
        except KeyError:
            self.fail('Test fails because nickname or color is not set')
