from django.contrib import admin

from .models import Content, PartnerAndView, Slide, OutputContent, MainpageSection, SocialMediaLink

# Register your models here.

admin.site.site_header = "Disaster Journalism Site Administration Panel"
admin.site.site_title = "Site Management"
admin.site.index_title = "Welcome to Admin Panel"


class SiteAdmin(admin.ModelAdmin):
  list_filter = ("numberpacket",)


#Sosyal medya linkleri
admin.site.register(SocialMediaLink)
admin.site.register(PartnerAndView)
admin.site.register(Content)

# Main page eklenen içerikler
admin.site.register(MainpageSection)
admin.site.register(OutputContent)
admin.site.register(Slide)

