from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Oluşturulan yazı, makale, haber, etkinlik yazıları için oluşturulan tablo yapısı
class ModelGuidebook(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(help_text="Image size should be '280x326'")
    file = models.FileField(upload_to="documents/workpackets/pdf")
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ModelNavbar(models.Model):
    title = models.CharField(max_length=100, help_text="Please just enter one of these words and follow this order: 'home, about, outputs, workpackages, news, partners, views, contact'.")
       
    def __str__(self):
        return self.title

# Ortakların isim, resim, site ve açıklama bilgilerini saklayan tablo yapısı
class ModelPartner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="partners/img", help_text="Image size should be '280x326'")
    website = models.URLField(max_length=150)
    description = RichTextField(config_name='custom')

    def __str__(self):
        return self.title

# Oluşturulan yazı, makale, haber, etkinlik yazıları için oluşturulan tablo yapısı
class ModelNews(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="news/img", help_text="Image size should be '420x316'")
    description = RichTextField(config_name='custom')
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    
# Videolar için oluşturulan tablo yapısı
class ModelVideo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="videos/img")
    URL = models.URLField(max_length=150)

    def __str__(self):
        return f"{self.title}"

# Galeri için oluşturulan tablo yapısı
class ModelGallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery/img")
    file = models.FileField(upload_to="gallery/pdf")

    def __str__(self):
        return f"{self.title}"

# Podcast için oluşturulan tablo yapısı
class ModelPodcast(models.Model):
    title = models.CharField(max_length=100)
    URL = models.URLField(max_length=150)

    def __str__(self):
        return f"{self.title}"
    
# İnsanların yorumları için oluşturulan tablo yapısı
class ModelView(models.Model):
    fullname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slides/img")
    description = models.TextField()

    def __str__(self):
        return f"{self.fullname}"
    

# Anasayfadaki video içeriği    

# Oluşturulan yazı, makale, haber, etkinlik yazıları için oluşturulan tablo yapısı
class ModelWorkpackage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="workpackets/img")
    description = RichTextField(config_name='custom')
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)  



# Anasayfada bulunan slayt yapısı için oluşturulan tablo
class Slide(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slides/img", help_text="Image size should be '1920x1080'.")
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"
    


class MainpageOutputContent(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('video', 'Video'),
        ('info', 'Info'),
        ('podcast', 'Podcast'),
        ('guidebook', 'Guidebook'),
    ]
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="videos/img", blank=True, null=True, help_text="NOTE: Image just needs for video and size should be '1920x1080'.")  # Sadece video için gerekli
    URL = models.URLField(max_length=150, blank=True, null=True, help_text="NOTE: URL just needs for video.")  # Sadece video için gerekli
    
    def __str__(self):
        return f"{self.content_type}: {self.title}"
    

class MainpageSection(models.Model):
    SECTION_CHOICES = [
        ('about', 'About Section'),
        ('output', 'Output Section'),
        ('workpackage', 'Workpackage Section'),
        ('news', 'News Section'),
        ('view', 'View Section'),
        # Diğer bölümler burada eklenebilir...
    ]
    section_type = models.CharField(max_length=20, choices=SECTION_CHOICES)
    header = models.CharField(max_length=100)
    backHeader = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return f"{self.section_type}: {self.header}"


class SocialMediaLink(models.Model):
    PLATFORM_CHOICES = [
        ('youtube', 'YouTube'),
        ('facebook', 'Facebook'),
        ('spotify', 'Spotify'),
        ('instagram', 'Instagram'),
        ('telegram', 'Telegram'),
        ('discord', 'Discord'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    URL = models.URLField(max_length=150)

    def __str__(self):
        return f"{self.get_platform_display()} - {self.URL}"