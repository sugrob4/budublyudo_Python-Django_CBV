from django.urls import path

from .views import LoginAuth, LogoutUser, Registration

urlpatterns = [
    path('login/', LoginAuth.as_view(), name="login"),
    path('logout/', LogoutUser.as_view(), name="logout"),
    path('registration/', Registration.as_view(), name="registration"),
]
