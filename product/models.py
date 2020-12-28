from __future__ import unicode_literals
from django.db import models

# for deletion of the attachments after deletion of object
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Product(models.Model) :

    product_name = models.CharField(max_length=250, null=True, blank=True)
    index = models.CharField(max_length=5, null=True, blank=True)
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    is_vsg = models.CharField(max_length=250, null=True, blank=True)
    is_paginate = models.CharField(max_length=250, null=True, blank=True)
    is_tab = models.CharField(max_length=250, null=True, blank=True)

    main_image = models.ImageField(upload_to='product', null=True, blank=True)

    def __str__(self) :

        return self.index + " | " + self.product_name

@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs) :
    instance.main_image.delete(False)


class Sheet(models.Model) :

    index = models.IntegerField(default=0, null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    main_finish = models.CharField(max_length=100, null=True, blank=True, default='')
    sub_finish = models.CharField(max_length=100, null=True, blank=True, default='')
    main_image = models.ImageField(upload_to='product/sheet', null=True, blank=True)
    fk = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) :

        return str(self.index) + " | " + str(self.number) + " | " + str(self.fk.product_name)


@receiver(post_delete, sender=Sheet)
def submission_delete2(sender, instance, **kwargs) :
    instance.main_image.delete(False)

    


