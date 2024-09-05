from django.shortcuts import render
from myapp.models import  FacebookLink, InstagramLink, MainpageGuidebook, MainpageInfo, MainpageNews, MainpageOutput, MainpagePodcast, MainpageVideo, MainpageView, MainpageWorkpacket, ModelGuidebook, MainpageAbout, ModelNavbar, ModelWorkPacket, SpotifyLink, WorkPacket, ModelPartner, MainpageSlide, NumberWorkPacket, ModelVideo, ModelPodcast, ModelNews, ModelGallery, ModelView, YoutubeLink
from django.conf import settings
#from myapp.forms import ContactForm

# Create your views here.

# Anasayfa için oluşturulan yapı. 
# Tüm tablolarla bağlantılı.
# Sitenin özetinin gösterildiği kısım
def custom_error_400(request, exception=None):
    return render(request, '404.html', {
    "navModels": ModelNavbar.objects.all(),
  }, status=400)

def custom_error_403(request, exception=None):
    return render(request, '404.html', {
    "navModels": ModelNavbar.objects.all(),
  }, status=403)

def custom_error_404(request, exception=None):
    return render(request, '404.html', '404.html', {
    "navModels": ModelNavbar.objects.all(),
  }, status=404)

def custom_error_500(request):
    return render(request, '404.html', {
    "navModels": ModelNavbar.objects.all(),
  }, status=500)



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
    "guideMains": MainpageGuidebook.objects.all(),
    "podcastMains": MainpagePodcast.objects.all(),
    "workpacketdenemes": ModelWorkPacket.objects.all(),

    
    "youtubeLinks": YoutubeLink.objects.all(),
    "faceLinks": FacebookLink.objects.all(),
    "spotifyLinks": SpotifyLink.objects.all(),
    "instaLinks": InstagramLink.objects.all(),
    
    "navModels": ModelNavbar.objects.all(),
    "partners": ModelPartner.objects.all(),
    "slides": MainpageSlide.objects.all(),
    "podcasts": ModelPodcast.objects.all(),
    "events": ModelNews.objects.all()[::-1],
    "gallerys": ModelGallery.objects.all(),
    "peoples": ModelView.objects.all(),
  }

  return render(request, "myapp/index.html", context)

# Video içeriği
def video(request):
  context = {
    "videos": ModelVideo.objects.all(),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/video.html", context)

# Etkinlik, haber, blog yazısı için içerik
def event(request):
  context = {
    "events": ModelNews.objects.all(),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/events.html", context)

# Tek blog yazısının gösterilmesi için oluşturulan yapı
def single_event(request, slug):
  
  single= ModelNews.objects.get(slug=slug)
  return render(request, "myapp/single-event.html",{
    'single': single,
    "navModels": ModelNavbar.objects.all(),
  })

# Podcast içeriği
def podcast(request):
  context = {
    
    "navModels": ModelNavbar.objects.all(),
    "podcasts": ModelPodcast.objects.all()
  }
  return render(request, "myapp/podcast.html", context)

# Gallery içeriği
def gallery(request):
  context = {
    "gallerys": ModelGallery.objects.all(),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/gallery.html", context)

# Workpacketların saklandığı yapı
def workpackets(request):
  context = {
    "workpacketdenemes" : ModelWorkPacket.objects.all(),
    "navModels": ModelNavbar.objects.all(),
    #"workpackets": WorkPacket.objects.all(),
    #"numberworkpackets": NumberWorkPacket.objects.all()
  }
  return render(request, "myapp/workpackets.html", context)

def single_workpacket(request, slug):
  single= ModelWorkPacket.objects.get(slug=slug)
  return render(request, "myapp/single-workpacket.html",{
    'single': single,
    "navModels": ModelNavbar.objects.all()
  })

# Etkinlik, haber, blog yazısı için içerik
def guidebook(request):
  context = {
    "guidebooks": ModelGuidebook.objects.all(),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/guidebook.html", context)

# Tek blog yazısının gösterilmesi için oluşturulan yapı
def single_guidebook(request, slug):
  single= ModelGuidebook.objects.get(slug=slug),
  return render(request, "myapp/single-guidebook.html",{
    'single': single,
    "navModels": ModelNavbar.objects.all()
  })






