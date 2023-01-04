from django.urls import path
from .views import Homepageview,Loginpageview

app_name = 'stdetails'

urlpatterns = [
    path('home/',Homepageview.as_view(),name = 'Homepage'),
    path('',Loginpageview.as_view(  ),name = 'loginpage'),
]
