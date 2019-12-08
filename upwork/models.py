from django.db import models

# Create your models here.
class Job(models.Model):
    job_url = models.fields.CharField(max_length=255)

    def __str__(self):
        return self.job_url

    def __repr__(self):
        return self.job_url