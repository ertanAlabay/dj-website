from django.shortcuts import render
from core.settings import EMAIL_HOST_USER
from myapp.models import  LinkFacebook, LinkInstagram, MainpageGuidebook, MainpageInfo, MainpageNews, MainpageOutput, MainpagePodcast, MainpageVideo, MainpageView, MainpageWorkpackage, ModelGuidebook, MainpageAbout, ModelNavbar, ModelWorkpackage, LinkSpotify, ModelPartner, MainpageSlide, ModelVideo, ModelPodcast, ModelNews, ModelGallery, ModelView, LinkYoutube
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
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

  success = request.session.pop('success', False)
  error = request.session.pop('error', False)

  if request.method == 'POST':
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        message = request.POST.get('textarea')

        if name and email and message:
            try:
                subject = f"New contact form submission from {name}"
                message_body = f"Name: {name}\nEmail: {email}\n\nMessage: \n{message}"

                # Mail gönderimi
                send_mail(
                    name,
                    message_body,
                    email,  # Gönderenin email adresi
                    [EMAIL_HOST_USER],  # Alıcı email adresi
                    fail_silently=False,
                )

                # Başarıyla gönderildikten sonra sayfaya GET isteği ile yönlendirme yapılacak
                return HttpResponseRedirect('/')

            except Exception as e:
                error = True
        else:
            error = True
    


  context = {
    'success': success,
    'error': error,

    "aboutMains": MainpageAbout.objects.all(),
    "outputMains": MainpageOutput.objects.all(),
    "workpacketMains": MainpageWorkpackage.objects.all(),
    "newsMains": MainpageNews.objects.all(),
    "guidebooks": ModelGuidebook.objects.all(),
    "viewMains": MainpageView.objects.all(),
    "videoMains": MainpageVideo.objects.all(),
    "infoMains": MainpageInfo.objects.all(),
    "guideMains": MainpageGuidebook.objects.all(),
    "podcastMains": MainpagePodcast.objects.all(),
    "workpacketModels": ModelWorkpackage.objects.all(),

    
    "youtubeLinks": LinkYoutube.objects.all(),
    "faceLinks": LinkFacebook.objects.all(),
    "spotifyLinks": LinkSpotify.objects.all(),
    "instaLinks": LinkInstagram.objects.all(),
    
    "navModels": ModelNavbar.objects.all(),
    "partners": ModelPartner.objects.all(),
    "slides": MainpageSlide.objects.all(),
    "podcasts": ModelPodcast.objects.all(),
    "news": ModelNews.objects.all()[::-1],
    "gallerys": ModelGallery.objects.all(),
    "peoples": ModelView.objects.all(),
  }

  return render(request, "myapp/index.html", context)

# Video içeriği
def videos(request):
  context = {
    "videos": ModelVideo.objects.all(),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/video.html", context)

# Etkinlik, haber, blog yazısı için içerik
def news(request):
  context = {
    "news": ModelNews.objects.all(),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/news.html", context)

# Tek blog yazısının gösterilmesi için oluşturulan yapı
def single_news(request, slug):
  
  single= ModelNews.objects.get(slug=slug)
  return render(request, "myapp/single-news.html",{
    'single': single,
    "navModels": ModelNavbar.objects.all(),
  })

# Podcast içeriği
def podcasts(request):
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
    "workpacketModels" : ModelWorkpackage.objects.all(),
    "navModels": ModelNavbar.objects.all(),
    #"workpackets": WorkPacket.objects.all(),
    #"numberworkpackets": NumberWorkPacket.objects.all()
  }
  return render(request, "myapp/workpackets.html", context)

def single_workpacket(request, slug):
  single= ModelWorkpackage.objects.get(slug=slug)
  return render(request, "myapp/single-workpacket.html",{
    'single': single,
    "navModels": ModelNavbar.objects.all()
  })

# Etkinlik, haber, blog yazısı için içerik
def guidebooks(request):
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






