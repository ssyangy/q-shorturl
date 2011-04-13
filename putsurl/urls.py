from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from surl.models import Surl

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^putsurl/', include('putsurl.foo.urls')),
	(r'^$','surl.views.putindex'),
	(r'^add/$','surl.views.add'),
	(r'^test/(?P<_surl>\w+)','surl.views.test'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
