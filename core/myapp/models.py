from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Anasayfada bulunan slayt yapısı için oluşturulan tablo
class Slide(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slides/img", help_text="Image size should be '1920x1080'.")
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"
    

class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('news', 'News'),
        ('podcast', 'Podcast'),
        ('video', 'Video'),
        ('workpackage', 'Workpackage'),
        ('gallery', 'Gallery'),
        ('guidebook', 'Guidebook'),
        ('rtuk', 'Rtuk'),
    ]

    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)  # Type of content (news, podcast, etc.)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="content/img", help_text="Image size should be relevant to content type")
    file = models.FileField(upload_to="content/files", null=True, blank=True, help_text="NOTE: file just needs for guidebooks.")  # Optional for types without files (news, podcast)
    URL = models.URLField(max_length=150, null=True, blank=True)  # Optional for types without URLs (news, workpackage, gallery)
    description = RichTextField(config_name='custom', null=True, blank=True)  # Optional for types without detailed description
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    
    def __str__(self):
        return f"{self.get_content_type_display()} / {self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class PartnerAndView(models.Model):
    ENTITY_TYPE_CHOICES = [
        ('partner', 'Partner'),
        ('view', 'View'),  # Review or Testimonial
    ]

    entity_type = models.CharField(max_length=20, choices=ENTITY_TYPE_CHOICES)  # Type of entity (partner or view)
    fullname = models.CharField(max_length=100, help_text="NOTE: Partners and Viewers name.")
    title = models.CharField(max_length=100, null=True, blank=True, help_text="NOTE: Just for the viws.")  # Partner's name or reviewer's name
    image = models.ImageField(upload_to="entity/img")
    website = models.URLField(max_length=150, null=True, blank=True, help_text="NOTE: website just needs for partners.")  # For partners
    description = models.TextField(null=True, blank=True)  # Description for partner or review
    
    def __str__(self):
        return f"{self.get_entity_type_display()} / {self.fullname}"
    



class OutputContent(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('video', 'Video'),
        ('info', 'Info'),
        ('podcast', 'Podcast'),
        ('guidebook', 'Guidebook'),
        ('rtuk', 'Rtuk'),
    ]
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="videos/img", blank=True, null=True, help_text="NOTE: Image just needs for video and size should be '1920x1080'.")  # Sadece video için gerekli
    URL = models.URLField(max_length=150, blank=True, null=True, help_text="NOTE: URL just needs for video.")  # Sadece video için gerekli
    
    def __str__(self):
        return f"{self.content_type} / {self.title}"
    

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
        return f"{self.section_type} / {self.header}"


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
        return f"{self.get_platform_display()} / {self.URL}"