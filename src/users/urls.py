from django.urls import include, path

from .views import RegistrationView


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("registration/", RegistrationView.as_view(), name="registration"),
]
