from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to, direct_to_template

urlpatterns = patterns('',
    # Examples:
    ('^$', direct_to_template, {'template' : 'index.html'}),
    url(r'^tasks/', include('tasks.urls')),
)
