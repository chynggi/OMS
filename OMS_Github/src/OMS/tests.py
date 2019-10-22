import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse   
from django.conf import settings as django_settings
from importlib import import_module


#이번 테스트 케이스는 모델 테스트를 모두 통과했다고 가정하고 작성한다.    
        
class SessionEnabledTestCase(TestCase): #code by dustinfarris

    def get_session(self):
        if self.client.session:
            session = self.client.session
        else:
            engine = import_module(django_settings.SESSION_ENGINE)
            session = engine.SessionStore()
        return session

    def set_session_cookies(self, session):
        # Set the cookie to represent the session
        session_cookie = django_settings.SESSION_COOKIE_NAME
        self.client.cookies[session_cookie] = session.session_key
        cookie_data = {
            'max-age': None,
            'path': '/',
            'domain': django_settings.SESSION_COOKIE_DOMAIN,
            'secure': django_settings.SESSION_COOKIE_SECURE or None,
            'expires': None}
        self.client.cookies[session_cookie].update(cookie_data)        



class ConnectionTests(SessionEnabledTestCase): 
    def test_login(self):
        response = self.client.get(reverse('OMS:login'))
        self.assertEqual(response.status_code, 200)
    def test_index(self):
        session = self.get_session()
        session['userid'] = 'admin'
        session.save()
        self.set_session_cookies(session)
        response = self.client.get(reverse('OMS:index'))
        self.assertTemplateUsed(response, template_name='OMS/Orders.html' )   
    def test_index2(self):
        session = self.get_session()
        session['userid'] = None
        session.save()
        self.set_session_cookies(session)
        response = self.client.get(reverse('OMS:index')) 
        self.assertTemplateUsed(response, template_name='OMS/index.html' )
    def test_logout(self):  
        session = self.get_session()
        session['userid'] = 'admin'
        session.save()
        self.set_session_cookies(session)
        response = self.client.get(reverse('OMS:logout'))        
        self.assertEqual(response.status_code, 302)  