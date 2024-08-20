from django.contrib import admin

from .models import MainpageAbout, MainpageGuidebook, MainpageInfo, MainpageNews, MainpageOutput, MainpagePodcast, MainpageVideo, MainpageView, MainpageWorkpacket, ModelGuidebook, ModelNavbar, ModelView, ModelWorkPacket, WorkPacket, Partner, Slide, Event, NumberWorkPacket, Video, Podcast, Gallery, People

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
admin.site.register(MainpageWorkpacket)
admin.site.register(MainpageNews)
admin.site.register(ModelView)
admin.site.register(ModelWorkPacket)
admin.site.register(ModelGuidebook)
admin.site.register(MainpageView)
admin.site.register(MainpageVideo)
admin.site.register(MainpageInfo)
admin.site.register(MainpagePodcast)
admin.site.register(MainpageGuidebook)

#admin.site.register(WorkPacket, SiteAdmin)
admin.site.register(Partner)
admin.site.register(Slide)
admin.site.register(Event)
#admin.site.register(NumberWorkPacket)
admin.site.register(Video)
admin.site.register(Podcast)
admin.site.register(Gallery)
admin.site.register(People)