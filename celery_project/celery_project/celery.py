from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from . import celery_settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_project.settings")

app = Celery("celery_project")

app.config_from_object(celery_settings)

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
