from django.urls import path

from . import views

app_name = "application"

urlpatterns = [
    path("email/", views.EmailView.as_view(), name="email_view"),
]
