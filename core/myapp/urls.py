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
    path("video", views.video, name="video"),
    path("gallery", views.gallery, name="gallery"),
    path("workpacket", views.workpackets),
    path("workpacket/<slug:slug>/", views.single_workpacket, name="workpacket_details"),
    path("podcast", views.podcast, name="podcast"),
    path("event", views.event, name="event"),
    path("event/<slug:slug>/", views.single_event, name="event_details" ),      
    path("guidebook", views.guidebook, name="guidebook"),
    path("guidebook/<slug:slug>/", views.single_guidebook, name="guidebook_details" ),      
]
