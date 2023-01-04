from django.urls import path
from .views import Homepageview

app_name = 'stdetails'

urlpatterns = [
    path('',Homepageview.as_view(),name = 'Homepage')
]
