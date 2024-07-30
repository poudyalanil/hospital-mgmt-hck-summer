from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    logo = models.ImageField(null=True, blank=True, upload_to="logos/")

    def __str__(self):
        return f"{self.name} {self.pk}"
