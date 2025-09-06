from django.urls import path

from django.contrib.auth.views import LogoutView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import PaymentListAPIView, CreateAPIView, profile_info, UserUpdateAPIView, UserRetrieveAPIView, \
    UserDestroyAPIView, UserListAPIView

app_name = 'users'

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CreateAPIView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='distribution:distributions'), name='logout'),
    path('profile/<int:pk>', profile_info, name='profile'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='update'),
    path('detail/<int:pk>', UserRetrieveAPIView.as_view(), name='detail'),
    path('delete/<int:pk>', UserDestroyAPIView.as_view(), name='delete'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
]