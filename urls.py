from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    # Examples:
    ('^$', redirect_to, {'url' : '/tasks/new'}),
    url(r'^tasks/', include('tasks.urls')),
)
