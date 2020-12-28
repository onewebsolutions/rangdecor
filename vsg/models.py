from django.db import models

# for deletion of the attachments after deletion of object
from django.db.models.signals import post_delete
from django.dispatch import receiver



class VSG(models.Model) :

    index = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    area_id = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to="vsg", null=True, blank=True)
    meta_title = models.CharField(max_length=150, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    is_show = models.CharField(max_length=25, null=True, blank=True)


    def __str__(self) :

        return self.index + " | " + self.area
        

@receiver(post_delete, sender=VSG)
def submission_delete(sender, instance, **kwargs) :
    instance.main_image.delete(False)


