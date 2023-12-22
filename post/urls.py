from rest_framework.urls import path

from .views import PostAPIView, PostDetailAPIView

urlpatterns = [
    path("", PostAPIView.as_view()),
    path("<int:pk>/", PostDetailAPIView.as_view())
]
