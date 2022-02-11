# Celery
# https://docs.celeryproject.org/en/stable/userguide/configuration.html
broker_url = "redis://redis:6379/0"
accept_content = ["json"]
task_serializer = "json"
result_serializer = "json"
timezone = "UTC" # UTC
result_backend = "django-db"
# result_backend = "django-db"
# beat_schedule = {
#     "send-email-every-minute": {
#         "task": "application.tasks.send_email_task",
#         "schedule": 60.0,
#         "kwargs": {
#             "name": "celery",
#             "email": "moin26944@gmail.com",
#             "subject": "Hello from Celery",
#             "message": "Email after 1 minute",
#         },
#     }
# }

# celery -A beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
