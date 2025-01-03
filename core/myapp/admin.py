from django.contrib import admin

from .models import LinkDiscord, LinkTelegram, LinkFacebook, LinkInstagram, MainpageAbout, MainpageGuidebook, MainpageInfo, MainpageNews, MainpageOutput, MainpagePodcast, MainpageVideo, MainpageView, MainpageWorkpackage, ModelGuidebook, ModelNavbar, ModelWorkpackage, LinkSpotify, ModelPartner, MainpageSlide, ModelNews, ModelVideo, ModelPodcast, ModelGallery, ModelView, LinkYoutube

# Register your models here.

admin.site.site_header = "Disaster Journalism Site Administration Panel"
admin.site.site_title = "Site Management"
admin.site.index_title = "Welcome to Admin Panel"


class SiteAdmin(admin.ModelAdmin):
  list_filter = ("numberpacket",)




admin.site.register(ModelNavbar)

# Main page eklenen içerikler
admin.site.register(MainpageAbout)
admin.site.register(MainpageOutput)
admin.site.register(MainpageWorkpackage)
admin.site.register(MainpageNews)
admin.site.register(MainpageView)
admin.site.register(MainpageVideo)
admin.site.register(MainpageInfo)
admin.site.register(MainpagePodcast)
admin.site.register(MainpageGuidebook)
admin.site.register(MainpageSlide)

#Sosyal medya linkleri
admin.site.register(LinkYoutube)
admin.site.register(LinkSpotify)
admin.site.register(LinkFacebook)
admin.site.register(LinkInstagram)
admin.site.register(LinkTelegram)
admin.site.register(LinkDiscord)

# Main page eklenen içerikler
admin.site.register(ModelPartner)
admin.site.register(ModelWorkpackage)
admin.site.register(ModelGuidebook)
admin.site.register(ModelNews)
admin.site.register(ModelVideo)
admin.site.register(ModelPodcast)
admin.site.register(ModelGallery)
admin.site.register(ModelView)
