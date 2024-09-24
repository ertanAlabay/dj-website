from django.contrib import admin

from .models import Slide, MainpageOutputContent, MainpageSection, ModelGuidebook, ModelNavbar, ModelWorkpackage, ModelPartner, ModelNews, ModelVideo, ModelPodcast, ModelGallery, ModelView, SocialMediaLink

# Register your models here.

admin.site.site_header = "Disaster Journalism Site Administration Panel"
admin.site.site_title = "Site Management"
admin.site.index_title = "Welcome to Admin Panel"


class SiteAdmin(admin.ModelAdmin):
  list_filter = ("numberpacket",)




admin.site.register(ModelNavbar)

#Sosyal medya linkleri
admin.site.register(SocialMediaLink)

# Main page eklenen içerikler
admin.site.register(MainpageSection)
admin.site.register(MainpageOutputContent)
admin.site.register(Slide)

# Main page eklenen içerikler
admin.site.register(ModelPartner)
admin.site.register(ModelWorkpackage)
admin.site.register(ModelGuidebook)
admin.site.register(ModelNews)
admin.site.register(ModelVideo)
admin.site.register(ModelPodcast)
admin.site.register(ModelGallery)
admin.site.register(ModelView)
