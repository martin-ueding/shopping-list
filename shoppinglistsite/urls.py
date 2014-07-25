from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'shoppinglistsite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'admin/', include(admin.site.urls)),
                       url(r'view/$', 'shoppinglist.views.view'),
                       url(r'aftermath/$', 'shoppinglist.views.aftermath'),
                       url(r'change/(?P<product_id>\d+)/(?P<delta>-?\d+)$', 'shoppinglist.views.change'),
                       url(r'^$', 'shoppinglist.views.index'),
                       url(r'product/add/(?P<shelf_id>\d+)$', 'shoppinglist.views.add_product'),
                       url(r'shelf/add$', 'shoppinglist.views.add_shelf'),
                      )
