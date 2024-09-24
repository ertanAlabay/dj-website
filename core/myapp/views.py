from django.shortcuts import render
from core.settings import EMAIL_HOST_USER
from myapp.models import ModelContent, ModelEntity, Slide, MainpageOutputContent, MainpageSection, ModelNavbar, SocialMediaLink
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
    
  # İçerikleri çekiyoruz
  videos = ModelContent.objects.filter(content_type='video')  # Video içeriklerini çekiyoruz
  news = ModelContent.objects.filter(content_type='news')    # Haber içeriklerini çekiyoruz
  galleries = ModelContent.objects.filter(content_type='gallery')  # Galeri içeriklerini çekiyoruz
  podcasts = ModelContent.objects.filter(content_type='podcast')  # Podcast içeriklerini çekiyoruz
  workpackages = ModelContent.objects.filter(content_type='workpackage')  # Workpackage içerikleri
  guidebooks = ModelContent.objects.filter(content_type='guidebook')  # Guidebook içerikleri

  # Ortaklar ve yorumlar
  partners = ModelEntity.objects.filter(entity_type='partner')  # Partnerleri çekiyoruz
  reviews = ModelEntity.objects.filter(entity_type='view')  # Yorumları çekiyoruz

  # Verileri şablona gönderiyoruz
    


  context = {
    'success': success,
    'error': error,

    'videos': videos,
    'news': news,
    'galleries': galleries,
    'podcasts': podcasts,
    'workpackages': workpackages,
    'partners': partners,
    'reviews': reviews,
    'guidebooks': guidebooks,

    "socialMediaLinks": SocialMediaLink.objects.all(),
    'about_sections': MainpageSection.objects.filter(section_type='about'),
    'output_sections': MainpageSection.objects.filter(section_type='output'),
    'workpackage_sections': MainpageSection.objects.filter(section_type='workpackage'),
    'news_sections': MainpageSection.objects.filter(section_type='news'),
    'view_sections': MainpageSection.objects.filter(section_type='view'),

    'outputContents': MainpageOutputContent.objects.all(),
    'slides': Slide.objects.all(),

    
    
  }

  return render(request, "myapp/index.html", context)

# Video içeriği
def videos(request):
  context = {
    "videos": ModelContent.objects.filter(content_type='video'),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/video.html", context)

# Etkinlik, haber, blog yazısı için içerik
def news(request):
  context = {
    "news": ModelContent.objects.filter(content_type='news'),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/news.html", context)

# Tek blog yazısının gösterilmesi için oluşturulan yapı
def single_news(request, slug):
  
  single= ModelContent.objects.filter(content_type='news').get(slug=slug)
  return render(request, "myapp/single-news.html",{
    'single': single,
    "navModels": ModelNavbar.objects.all(),
  })

# Podcast içeriği
def podcasts(request):
  context = {
    
    "navModels": ModelNavbar.objects.all(),
    "podcasts": ModelContent.objects.filter(content_type='podcast')
  }
  return render(request, "myapp/podcast.html", context)

# Gallery içeriği
def gallery(request):
  context = {
    "galleries": ModelContent.objects.filter(content_type='gallery'),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/gallery.html", context)

# Workpacketların saklandığı yapı
def workpackets(request):
  context = {
    "workpackages" : ModelContent.objects.filter(content_type='workpackage'),
    "navModels": ModelNavbar.objects.all(),
    #"workpackets": WorkPacket.objects.all(),
    #"numberworkpackets": NumberWorkPacket.objects.all()
  }
  return render(request, "myapp/workpackets.html", context)

def single_workpacket(request, slug):
  single= ModelContent.objects.filter(content_type='workpackage').get(slug=slug)
  return render(request, "myapp/single-workpacket.html",{
    'single': single,
    "navModels": ModelNavbar.objects.all()
  })

# Etkinlik, haber, blog yazısı için içerik
def guidebooks(request):
  context = {
    "guidebooks": ModelContent.objects.filter(content_type='guidebook'),
    "navModels": ModelNavbar.objects.all(),
  }
  return render(request, "myapp/guidebook.html", context)

# Tek blog yazısının gösterilmesi için oluşturulan yapı
def single_guidebook(request, slug):
  single= ModelContent.objects.filter(content_type='guidebook').get(slug=slug),
  return render(request, "myapp/single-guidebook.html",{
    'single': single,
    "navModels": ModelNavbar.objects.all()
  })






