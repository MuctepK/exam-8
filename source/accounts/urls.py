from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import register_view, UserDetailView, UserChangeView, UserChangePasswordView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='register'),
    path('user/<int:pk>/detail/', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', UserChangeView.as_view(), name='user_update'),
    path('user/<int:pk>/change-password/', UserChangePasswordView.as_view(), name='user_change_password')

]

app_name = 'accounts'