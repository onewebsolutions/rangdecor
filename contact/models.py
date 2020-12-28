from __future__ import unicode_literals
from django.db import models



class Lead(models.Model): 

    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    time = models.CharField(max_length=250, null=True, blank=True)
    revert = models.BooleanField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + ' | ' + self.email


class Contact_Us(models.Model) :

    meta_title = models.CharField(max_length=200, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meta_title