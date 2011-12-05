from django.db import models

class Task(models.Model):
    content = models.CharField(max_length = 255)
    complete = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

    @models.permalink
    def get_absolute_url(self):
        return ('task', [self.pk])

    def as_json(self):
        return dict(
                content = self.content,
                complete = self.complete,
                created_at = str(self.created_at),
                id = self.pk
                )
