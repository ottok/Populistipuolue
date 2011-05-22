# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.utils.encoding import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('povastausanalyysi.views',
    (r"^$", 'index'),
    (r"^tutkimus$", 'tutkimus'),
    (r"^index.json$", 'index_json'),
)

urlpatterns += patterns('django.views',
    (r'^static/(?P<path>.*)$', 'static.serve',
        {'document_root': smart_unicode(settings.MEDIA_ROOT, encoding='utf-8', strings_only=False, errors='strict')}),


    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
