from django.contrib import admin

from .models import MainpageAbout, MainpageInfo, MainpageNews, MainpageOutput, MainpagePodcast, MainpageVideo, MainpageView, MainpageWorkpacket, ModelView, WorkPacket, Partner, Slide, Event, NumberWorkPacket, Video, Podcast, Gallery, People

# Register your models here.

class SiteAdmin(admin.ModelAdmin):
  list_filter = ("numberpacket",)

# Main page eklenen içerikler
admin.site.register(MainpageAbout)
admin.site.register(MainpageOutput)
admin.site.register(MainpageWorkpacket)
admin.site.register(MainpageNews)
admin.site.register(ModelView)
admin.site.register(MainpageView)
admin.site.register(MainpageVideo)
admin.site.register(MainpageInfo)
admin.site.register(MainpagePodcast)

admin.site.register(WorkPacket, SiteAdmin)
admin.site.register(Partner)
admin.site.register(Slide)
admin.site.register(Event)
admin.site.register(NumberWorkPacket)
admin.site.register(Video)
admin.site.register(Podcast)
admin.site.register(Gallery)
admin.site.register(People)