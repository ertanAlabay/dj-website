from django.shortcuts import render
from myapp.models import  MainpageInfo, MainpageNews, MainpageOutput, MainpagePodcast, MainpageVideo, MainpageView, MainpageWorkpacket, ModelGuidebook, MainpageAbout, ModelView, WorkPacket, Partner, Slide, NumberWorkPacket, Video, Podcast, Event, Gallery, People
from django.conf import settings
#from myapp.forms import ContactForm

# Create your views here.

# Anasayfa için oluşturulan yapı. 
# Tüm tablolarla bağlantılı.
# Sitenin özetinin gösterildiği kısım
def index(request):
  context = {

    "aboutMains": MainpageAbout.objects.all(),
    "outputMains": MainpageOutput.objects.all(),
    "workpacketMains": MainpageWorkpacket.objects.all(),
    "newsMains": MainpageNews.objects.all(),
    "guidebooks": ModelGuidebook.objects.all(),
    "viewMains": MainpageView.objects.all(),
    "videoMains": MainpageVideo.objects.all(),
    "infoMains": MainpageInfo.objects.all(),
    "podcastMains": MainpagePodcast.objects.all(),


    "workpackets": WorkPacket.objects.all(),
    "partners": Partner.objects.all(),
    "slides": Slide.objects.all(),
    "numberworkpackets": NumberWorkPacket.objects.all(),
    "podcasts": Podcast.objects.all(),
    "events": Event.objects.all(),
    "gallerys": Gallery.objects.all(),
    "peoples": People.objects.all(),
  }

  return render(request, "myapp/index.html", context)

# Video içeriği
def video(request):
  context = {
    "videos": Video.objects.all()
  }
  return render(request, "myapp/video.html", context)

# Etkinlik, haber, blog yazısı için içerik
def event(request):
  context = {
    "events": Event.objects.all()
  }
  return render(request, "myapp/events.html", context)

# Tek blog yazısının gösterilmesi için oluşturulan yapı
def single_event(request, slug):
  single= Event.objects.get(slug=slug)
  return render(request, "myapp/single-event.html",{
    'single': single
  })

# Podcast içeriği
def podcast(request):
  context = {
    "podcasts": Podcast.objects.all()
  }
  return render(request, "myapp/podcast.html", context)

# Gallery içeriği
def gallery(request):
  context = {
    "gallerys": Gallery.objects.all()
  }
  return render(request, "myapp/gallery.html", context)

# Workpacketların saklandığı yapı
def workpackets(request):
  context = {
    "workpackets": WorkPacket.objects.filter(),
    "numberworkpackets": NumberWorkPacket.objects.all()
  }
  return render(request, "myapp/workpackets.html", context)

# Workpacket kategori yapısı için
def workpacket_by_number(request, slug):
  context = {
    "workpackets": WorkPacket.objects.filter(numberpacket__slug=slug),
    "numberworkpackets": NumberWorkPacket.objects.all()
  }
  return render(request, "myapp/workpackets.html", context)