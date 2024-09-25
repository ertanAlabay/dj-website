from django.contrib import admin

from .models import Content, PartnerAndView, Slide, MainpageOutputContent, MainpageSection, Navbar, SocialMediaLink

# Register your models here.

admin.site.site_header = "Disaster Journalism Site Administration Panel"
admin.site.site_title = "Site Management"
admin.site.index_title = "Welcome to Admin Panel"


class SiteAdmin(admin.ModelAdmin):
  list_filter = ("numberpacket",)




admin.site.register(Navbar)

#Sosyal medya linkleri
admin.site.register(SocialMediaLink)
admin.site.register(PartnerAndView)
admin.site.register(Content)

# Main page eklenen içerikler
admin.site.register(MainpageSection)
admin.site.register(MainpageOutputContent)
admin.site.register(Slide)

