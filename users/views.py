from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from users.forms import CustomUserCreationForm
from users.models import Payment, CustomUser
from users.serializers import PaymentSerializer, UserSerializer


# Create your views here.
class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_course', 'payment_lesson', 'method_payment',)
    ordering_fields = ('date_pay',)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()


def profile_info(request, pk):
    user = CustomUser.objects.get(pk=pk)
    context = {'email': user.email,
               'phone': user.phone_number,
               'city': user.city,
               'pk': user.pk,
               }
    template_name = 'profile.html'
    return render(request, template_name, context)


