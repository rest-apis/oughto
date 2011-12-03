from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tasks.views', 
        url('^$',                      '_collection', name = "tasks"),
        url('^new$',                   'new'        , name = 'new_task'),
        url('^(?P<task_id>\d+)/edit$', 'edit'       , name = "edit_task"),
        url('^(?P<task_id>\d+)$',      '_member'    , name = "task")
)
