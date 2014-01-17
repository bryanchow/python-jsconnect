from django.conf.urls import patterns, url
from .views import jsconnect


urlpatterns = patterns('',

    url(r'^$', jsconnect, name='jsconnect'),

)
