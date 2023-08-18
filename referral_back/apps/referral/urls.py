from django.urls import path

from apps.referral.api.referral_viewset import ReferralViewSet

urlpatterns = [
    path('activate_invite_code/', ReferralViewSet.as_view({'post': 'activate_invite_code'})),
    path('get_referrals/', ReferralViewSet.as_view({'get': 'get_referrals'}))
]
