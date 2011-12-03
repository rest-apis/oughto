from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tasks.views', 
        url('^$',                      '_collection', name = "tasks"),
        url('^(?P<task_id>\d+)$',      '_member'    , name = "task")
)
