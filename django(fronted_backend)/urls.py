#coding: utf-8 

from django.conf.urls.defaults import patterns, include, url
from irkonline.search import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', views.search),
                       (r'look/$', views.autocompleteSearch),
                       (r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
#                       (r'^$', views.user_lookup),
#                        (r'^auto/$', views.ajax_search)
#                       (r'^q=[^/]+/(?P<j>\d{1,2})/$', views.autocomplete),
			(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:\djpr\irkonline\static'}),
    # Examples:
    # url(r'^$', 'irkonline.views.home', name='home'),
    # url(r'^irkonline/', include('irkonline.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()