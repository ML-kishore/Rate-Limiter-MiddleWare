from django.db import models

# Create your models here.
class RequestLogs(models.Model):
    ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['ip','timestamp'])]