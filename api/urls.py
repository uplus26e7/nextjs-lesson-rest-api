from django.conf.urls import include
from django.urls import path
from rest_framework import routers, urlpatterns

from api.views import (
    CreateUserView,
    PostListView,
    PostRetrieveView,
    TaskListView,
    TaskRetrieveView,
    TaskViewSet,
)

router = routers.DefaultRouter()

router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("list-post/", PostListView.as_view(), name="list-post"),
    path("detail-post/<str:pk>/", PostRetrieveView.as_view(), name="detail-post"),
    path("list-task/", TaskListView.as_view(), name="list-task"),
    path("detail-task/<str:pk>/", TaskRetrieveView.as_view(), name="detail-task"),
    path("register/", CreateUserView.as_view(), name="register"),
    path("auth/", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]
