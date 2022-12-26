from django.contrib import admin
from app.models import *
# Register your models here.
admin.site.register(Topic)
class webpages_venkey(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_editable=['url']
    list_display_links=['name','topic_name']
    list_per_page=2
    search_fields=['topic_name']
    list_filter=['name','topic_name']
admin.site.register(webpages,webpages_venkey)
admin.site.register(A_R)