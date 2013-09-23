from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bp_example.views.home', name='home'),
    url(r'^$', 'todo.views.home', name='home'),
    url(r'^delete/$', 'todo.views.delete', name='delete'),
    url(r'^add/$', 'todo.views.add', name='add'),
    # url(r'^bp_example/', include('bp_example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)