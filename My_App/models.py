from django.db import models

class client(models.Model):
    client_name = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=15)


    def __str__(self):
        return self.client_name
