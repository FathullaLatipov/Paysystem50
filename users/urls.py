from django.urls import path

from users.views import *

urlpatterns = [
    path('users/', UserModelListAPIView.as_view()),
    path('users/create', UserModelCreateAPIView.as_view()),
    path('users/update/<int:pk>', UserModelUpdateAPIView.as_view()),
    path('users/get/<int:pk>', UserModelRetrieveAPIView.as_view()),
    path('users/delete/<int:pk>', UserModelDestroyAPIView.as_view()),
]