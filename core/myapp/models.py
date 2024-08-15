from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

# Workpacketların kategorize etmek için ilişki kullanarak oluşturduğumuz tablo
# "Workpacket" tablosuyla "numberpacket" sütunu ilişkilendirilmiştir.  
# Kategori kullanarak filtrelemek için iki tabloda da "slugify" kullanılmıştır.
class NumberWorkPacket(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="number_workpacket/img")
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)
    
    def __str__(self):
        return f"{self.title}"
    
# Workpacketların card yapısında kullanılacak db tablosu
class WorkPacket(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="workpackets/img")
    description = models.TextField()
    file = models.FileField(upload_to="workpackets/pdf")
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)    
    numberpacket = models.ForeignKey(NumberWorkPacket, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    





# Ortakların isim, resim, site ve açıklama bilgilerini saklayan tablo yapısı
class Partner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="partners/img")
    website = models.URLField(max_length=150)
    description = RichTextField()

    def __str__(self):
        return self.title

# Oluşturulan yazı, makale, haber, etkinlik yazıları için oluşturulan tablo yapısı
class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = RichTextField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# Anasayfada bulunan slayt yapısı için oluşturulan tablo
class Slide(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slides/img")
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"
    
# Videolar için oluşturulan tablo yapısı
class Video(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="videos/img")
    URL = models.URLField(max_length=150)

    def __str__(self):
        return f"{self.title}"

# Galeri için oluşturulan tablo yapısı
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery/img")
    file = models.FileField(upload_to="gallery/pdf")

    def __str__(self):
        return f"{self.title}"

# Podcast için oluşturulan tablo yapısı
class Podcast(models.Model):
    title = models.CharField(max_length=100)
    URL = models.URLField(max_length=150)

    def __str__(self):
        return f"{self.title}"
    
# İnsanların yorumları için oluşturulan tablo yapısı
class People(models.Model):
    fullname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slides/img")
    description = models.TextField()

    def __str__(self):
        return f"{self.fullname}"
    

    

# Oluşturulan yazı, makale, haber, etkinlik yazıları için oluşturulan tablo yapısı
class ModelGuidebook(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = RichTextField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ModelView(models.Model):
    fullname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slides/img")
    description = models.TextField()

    def __str__(self):
        return f"{self.fullname}"

# Anasayfadaki video içeriği


class MainpageAbout(models.Model):
    header = models.CharField(max_length=100)
    backHeader = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return f"{self.header}"
    
class MainpageOutput(models.Model):
    header = models.CharField(max_length=100)
    backHeader = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return f"{self.header}"
    

class MainpageVideo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="videos/img")
    URL = models.URLField(max_length=150)

    def __str__(self):
        return f"{self.title}"    
    

class MainpageVideo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="videos/img")
    URL = models.URLField(max_length=150)

    def __str__(self):
        return f"{self.title}" 


class MainpageInfo(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title}" 

class MainpagePodcast(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title}" 
    

class MainpageWorkpacket(models.Model):
    header = models.CharField(max_length=100)
    backHeader = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return f"{self.header}"
    

class MainpageNews(models.Model):
    header = models.CharField(max_length=100)
    backHeader = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return f"{self.header}"
    

class MainpageView(models.Model):
    header = models.CharField(max_length=100)
    backHeader = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return f"{self.header}"