from django.contrib import admin

from .models import WorkPacket, Partner, Slide, Event, NumberWorkPacket, Video, Podcast, Gallery, People

# Register your models here.

class SiteAdmin(admin.ModelAdmin):
  list_filter = ("numberpacket",)

admin.site.register(WorkPacket, SiteAdmin)
admin.site.register(Partner)
admin.site.register(Slide)
admin.site.register(Event)
admin.site.register(NumberWorkPacket)
admin.site.register(Video)
admin.site.register(Podcast)
admin.site.register(Gallery)
admin.site.register(People)