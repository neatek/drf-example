import json
from todo.models import Project, Todo
from users.models import User as UserMistake
from todo.views import ProjectViewset, TodoViewset
from users.views import UserModelViewSet
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate,\
    APIClient, APISimpleTestCase, APITestCase

'''
    python manage.py test

    A quick implementation of simple API tests using:
        APIRequestFactory, APIClient, APITestCase

    ======================================================================
    FAIL: test_edit_mixer (todo.tests.TestBookViewSet)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "...\todo\tests.py", line 89, in test_edit_mixer
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    AssertionError: 404 != 200

    ======================================================================
    FAIL: test_create_guest (todo.tests.TestUserModelViewSet)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "...\todo\tests.py", line 37, in test_create_guest
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    AssertionError: 201 != 401

    ----------------------------------------------------------------------
    Ran 8 tests in 1.127s

    FAILED (failures=2)
    Destroying test database for alias 'default'...
'''

userTestParams = {'username': '1',
                  'firstname': '2',
                  'lastname': '3',
                  'email': '4'}


class TestUserModelViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', userTestParams, format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', userTestParams, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'admin123456')
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = UserMistake.objects.create(
            username='1', firstname='2', lastname='3', email='4')
        client = APIClient()
        response = client.get(f'/api/users/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        author = UserMistake.objects.create(
            username='1', firstname='2', lastname='3', email='4')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/users/{author.id}/', userTestParams)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = UserMistake.objects.get(id=author.id)
        self.assertEqual(author.username, '1')
        self.assertEqual(author.firstname, '2')
        client.logout()


class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestBookViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_mixer(self):
        user = mixer.blend(User)
        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(
            f'/api/users/{user.id}/', userTestParams)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.name, '1')
