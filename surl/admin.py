from surl.models import Surl
from django.contrib import admin

class SurlAdmin(admin.ModelAdmin):
	list_display=('surl','lurl','fingerprint','add_date')

admin.site.register(Surl,SurlAdmin)
