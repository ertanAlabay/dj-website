from django.conf.urls import handler404, handler500, handler403, handler400
from django.urls import path
from . import views


handler404 = 'myapp.views.custom_error_404'
handler500 = 'myapp.views.custom_error_500'
handler403 = 'myapp.views.custom_error_403'
handler400 = 'myapp.views.custom_error_400'


urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.index),
    path("videos", views.videos, name="video"),
    path("gallery", views.gallery, name="gallery"),
    path("workpackets", views.workpackets),
    path("workpackets/<slug:slug>/", views.single_workpacket, name="workpacket_details"),
    path("podcast", views.podcasts, name="podcast"),
    path("news", views.news, name="event"),
    path("news/<slug:slug>/", views.single_news, name="news_details" ),      
    path("guidebooks", views.guidebooks, name="guidebook"),
    path("guidebook/<slug:slug>/", views.single_guidebook, name="guidebook_details" ),      
]
