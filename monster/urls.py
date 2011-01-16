from django.conf.urls.defaults import *
from monster.views import show_fight

urlpatterns = patterns('',
                       url(r'^fight/', show_fight, name='fight'), 
)
