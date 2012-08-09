from django.conf.urls.defaults import *

urlpatterns = patterns('{{ app_name }}.views',
        url(r'^(?P<pk>\S{1,7})/$', "views.", name=""),
)
