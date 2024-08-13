from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.index),
    path("video", views.video, name="video"),
    path("gallery", views.gallery, name="gallery"),
    path("workpacket", views.workpackets),
    path("workpacket/<slug:slug>/", views.workpacket_by_number, name="workpacket_by_number"),
    path("podcast", views.podcast, name="podcast"),
    path("event", views.event, name="event"),
    path("event/<slug:slug>/", views.single_event, name="event_details" ),      
]
