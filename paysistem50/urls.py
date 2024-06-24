from django.contrib import admin
from django.urls import path, include

from users.views import *
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('card/', include('users.card_urls')),
    path('transfer/', include('users.transfer_urls')),
    path('test/', TestAPIView.as_view()),
    path('home/', hello_world)
]

urlpatterns += doc_urls
