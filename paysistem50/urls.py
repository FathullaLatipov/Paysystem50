from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings
from django.conf.urls.static import static
# python manage.py collectstatic
from users.views import *

from .yasg import urlpatterns as doc_urls

from .security import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include('users.urls')),
    path('card/', include('users.card_urls')),
    path('transfer/', include('users.transfer_urls')),
    path('test/', TestAPIView.as_view()),
    path('home/', hello_world),
    path('accounts/login/', login_view, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test-jwt/', Home.as_view()),
]

urlpatterns += doc_urls

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
