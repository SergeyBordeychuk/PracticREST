from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscription
from users.models import CustomUser

# Create your tests here.

class TestLesson(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='admin', email='admin@gmail.com', password='admin')
        self.client.force_authenticate(self.user)
        self.course1 = Course.objects.create(name_course='course1', owner=self.user)
        self.course2 = Course.objects.create(name_course='course2', owner=self.user)
        self.lesson1 = Lesson.objects.create(name_lesson='lesson1', course_id=self.course2.pk, owner=self.user)


    def test_lesson_create(self):
        data = {
            'name_lesson': 'lesson',
            'owner': self.user.pk,
            'link': 'http://youtube.com',
            'course': self.course1.pk,
        }
        response = self.client.post('/materials/lesson/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_update(self):
        self.course2 = Course.objects.create(name_course='course2', owner=self.user)
        self.lesson1 = Lesson.objects.create(name_lesson='lesson1', course_id=self.course2.pk, owner=self.user)
        data = {
            'name_lesson': 'lesson3',
            'owner': self.user.pk,
            'link': 'http://youtube.com',
            'course': self.course1.pk,
        }
        response = self.client.put('/materials/lesson/update/1', data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete(self):
        response = self.client.delete('/materials/lesson/delete/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestSubscription(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='admin', email='admin@gmail.com', password='admin')
        self.client.force_authenticate(self.user)
        self.course = Course.objects.create(name_course='course', owner=self.user)
        self.sub = Subscription.objects.create(user=self.user, course=self.course)


    def test_subscription(self):
        response = self.client.put('/materials/sub/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
