from django.conf.urls.defaults import *
from django.views.generic import ListView
from SOS.models import Product
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('SOS.views',
	(r'^$', 'index'),
	(r'^(?P<session_action>login|logout)/$', 'login_view'),
	(r'^products/$', ListView.as_view(
		model=Product,
		context_object_name="product_list",
		template_name="list.html",	
	))
)

urlpatterns += staticfiles_urlpatterns()