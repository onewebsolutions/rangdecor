from django.db import models

# for deletion of the attachments after deletion of object
from django.db.models.signals import post_delete
from django.dispatch import receiver





class Catalogue(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    name_id = models.CharField(max_length=150, null=True, blank=True)
    page_first = models.IntegerField(null=True, blank=True)
    page_second = models.IntegerField(null=True, blank=True)
    page_height = models.IntegerField(null=True, blank=True)
    page_width = models.IntegerField(null=True, blank=True)
    main_image_1 = models.ImageField(upload_to="catalogue", null=True, blank=True)
    main_image_2 = models.ImageField(upload_to="catalogue", null=True, blank=True)
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)

    def __str__(self) :

        return str(self.index) + " | " + self.name

@receiver(post_delete, sender=Catalogue)
def submission_delete(sender, instance, **kwargs) :
    instance.main_image.delete(False)


class Catalogue_Page(models.Model) :
    
    fk = models.ForeignKey(Catalogue, on_delete=models.PROTECT, null=True, blank=True)
    index = models.IntegerField(null=True, blank=True)
    page_first = models.IntegerField(null=True, blank=True)
    page_second = models.IntegerField(null=True, blank=True)
    main_image_1 = models.ImageField(upload_to="catalogue", null=True, blank=True)
    main_image_2 = models.ImageField(upload_to="catalogue", null=True, blank=True)

    def __str__(self) :
        return self.fk.name + " | " + str(self.index)

@receiver(post_delete, sender=Catalogue_Page)
def submission_delete_2(sender, instance, **kwargs) :
    instance.main_image_1.delete(False)
    instance.main_image_2.delete(False)




