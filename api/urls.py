from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from passport.views import BarsaViewSet, ProfileViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'passports', BarsaViewSet, basename='passports')
router.register(r'login', ProfileViewSet, basename='login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)