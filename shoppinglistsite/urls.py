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
                       url(r'update/$', 'shoppinglist.views.update_numbers'),
                       url(r'^$', 'shoppinglist.views.index'),
                       url(r'product/add$', 'shoppinglist.views_product.add'),
                       url(r'product$', 'shoppinglist.views_product.index'),
                       url(r'product/add/(?P<shelf_id>\d+)$', 'shoppinglist.views_product.add'),
                       url(r'shelf/add$', 'shoppinglist.views.add_shelf'),
                       url(r'product/order-more/(?P<product_id_str>\d+)$', 'shoppinglist.views_product.order_more'),
                       url(r'product/edit/(?P<product_id_str>\d+)$', 'shoppinglist.views_product.edit'),
                       url(r'product/order-more/(?P<product_id_str>\d+)/(?P<delta>\d+)$', 'shoppinglist.views_product.increment'),
                       url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'shoppinglist/templates/login.html'}),
                      )
