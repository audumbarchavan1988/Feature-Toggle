from django.db import models

class FeatureToggle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    enabled = models.BooleanField(default=False)
    is_global = models.BooleanField(default=False)
    owner = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)
    environment = models.ForeignKey('Environment', on_delete=models.CASCADE, null=True, blank=True)
    application = models.ForeignKey('Application', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Environment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
