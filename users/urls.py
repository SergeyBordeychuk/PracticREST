from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from users.views import PaymentListAPIView

app_name = 'users'

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
]