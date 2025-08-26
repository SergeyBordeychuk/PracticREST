from django.urls import path

from django.contrib.auth.views import LogoutView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import PaymentListAPIView, CreateAPIView, profile_info

app_name = 'users'

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('login/', TokenObtainPairView.as_view(permission_clases=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_clases=(AllowAny,)), name='token_refresh'),
    path('register/', CreateAPIView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='distribution:distributions'), name='logout'),
    path('profile/<int:pk>', profile_info, name='profile'),
]