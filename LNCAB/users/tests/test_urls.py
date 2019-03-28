from django.urls import reverse, resolve
from django.test import TestCase

#URL TESTING
class TestUrls():
    #Andres Quiroz A01400033
    def test_loggedUser(self):
        path = reverse('logged_user', kwargs = {'pk':1})
        assert resolve(path).view_name == 'logged_user'


    def test_loggedOutUser(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'

    def test_CreateUser(self):
        path = reverse('registerUser')
        assert resolve(path).view_name == 'registerUser'

    def test_CreatePlayer(self):
        path = reverse('registerPlayer')
        assert resolve(path).view_name == 'registerPlayer'

    def test_Logout(self):
        path = reverse('logout')
        assert resolve(path).view_name == 'logout'

   # def test_Login(self):
    #    path = reverse('login')
     #   assert resolve(path).view_name == 'user_login'





