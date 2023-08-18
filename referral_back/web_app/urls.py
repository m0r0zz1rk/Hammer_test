from django.contrib import admin
from django.urls import path, include
from .vars.yasg import urlpatterns as yasg_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('apps.authen.urls')),
    path('api/v1/referral/', include('apps.referral.urls')),
]
urlpatterns += yasg_urlpatterns
