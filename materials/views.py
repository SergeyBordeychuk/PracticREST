from django.shortcuts import redirect
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.paginators import CourseLessonPagination
from materials.permissions import IsModer, IsOwner
from materials.serializers import CourseSerializer, LessonSerializer, SubSerializer

from .services import  create_product, create_price_product, create_session


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CourseLessonPagination

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModer, IsAuthenticated)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModer | IsOwner, IsAuthenticated)
        elif self.action in ['retrieve', 'update']:
            self.permission_classes = (IsModer | IsOwner, IsAuthenticated)
        return super().get_permissions()

    def post(self, request, *args, **kwargs):
        product = create_product(request)
        price = create_price_product(request, product)
        session = create_session(request, product)
        return redirect(session['url'])


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [~IsModer | IsOwner, IsAuthenticated]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModer,]
    pagination_class = CourseLessonPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModer | IsOwner, IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModer | IsOwner, IsAuthenticated]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [~IsModer | IsOwner, IsAuthenticated]


class SubscriptionApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubSerializer

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        sub = Subscription.objects.filter(user=request.user, course=course).first()
        if sub:
            sub.delete()
            msg = 'Подписка удалена'
        else:
            Subscription.objects.create(user=request.user, course=course)
            msg = 'Подписка добавлена'
        return Response({'message': msg})
