from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template 
import os
static = os.path.join(os.path.dirname(__file__), 'static')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': static}),
)
