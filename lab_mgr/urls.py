from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from lab_mgr.admin import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab_mgr.views.home', name='home'),
    # url(r'^lab_mgr/', include('lab_mgr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(mysite.urls)),
)

if 'SERVER_SOFTWARE' in os.environ:
    urlpatterns += staticfiles_urlpatterns()
else:
    pass
