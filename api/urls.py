from django.urls import path

from api import views

urlpatterns = [
    path("stu/", views.StudentAPIView.as_view()),
    path("stu/<str:id>/", views.StudentAPIView.as_view()),
]
