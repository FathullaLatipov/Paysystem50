from django.urls import path

from users.views import *

urlpatterns = [
    path('cart/', UserCartListAPIView.as_view()),
    path('cart/create', UserCartCreateAPIView.as_view()),
    path('cart/update/<int:pk>', UserCartUpdateAPIView.as_view()),
    path('cart/retrieve/<int:pk>', UserCartRetrieveAPIView.as_view()),
    path('cart/delete/<int:pk>', UserCartDestroyAPIView.as_view()),
]