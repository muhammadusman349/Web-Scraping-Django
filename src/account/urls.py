from django.urls import path
from .views import SignupView, SigninView, index

urlpatterns = [
    path("", index, name="index"),
    path('signup/', SignupView.as_view(), name="signup-view"),
    path('signin/', SigninView.as_view(), name="signin-view"),
]
