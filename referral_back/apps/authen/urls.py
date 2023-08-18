from django.urls import path

from apps.authen.api.authorization_viewset import AuthorizationViewSet
from apps.authen.api.profile_viewset import ProfileViewSet

auth_urlpatterns = [
    path('check_auth/', AuthorizationViewSet.as_view({'get': 'check_auth'})),
    path('auth_request/', AuthorizationViewSet.as_view({'post': 'send_auth_request'})),
    path('login/', AuthorizationViewSet.as_view({'post': 'user_authorization'}))
]

profile_urlpatterns = [
    path('profile/', ProfileViewSet.as_view({'get': 'get_profile'}))
]

urlpatterns = auth_urlpatterns + profile_urlpatterns
