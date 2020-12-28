from django.db import models

# for deletion of the attachments after deletion of object
from django.db.models.signals import post_delete
from django.dispatch import receiver





class Page_Handler(models.Model) :

    index = models.CharField(max_length=10, null=True, blank=True)
    page_name = models.CharField(max_length=100, null=True, blank=True)
    page_info = models.TextField(null=True, blank=True)
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)

    def __str__(self) : 

        return self.index + " | " + self.page_name + '(' + str(self.pk ) + ')'   




class Looper_Section(models.Model) :

    fk = models.ForeignKey(Page_Handler, on_delete=models.SET_NULL, null=True, blank=True)
    page_name = models.CharField(max_length=100, null=True, blank=True)
    index = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) :

        return self.index + '  | ' + self.page_name + '(' + str(self.fk.pk ) + ')' + ' | ' + self.name


class Looper_Component(models.Model) :

    fk = models.ForeignKey(Looper_Section, on_delete=models.CASCADE, null=True, blank=True)
    page_name = models.CharField(max_length=100, null=True, blank=True)
    section_name = models.CharField(max_length=100, null=True, blank=True)
    index = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='looper', null=True, blank=True)
    second_image = models.ImageField(upload_to='looper', null=True, blank=True)
    third_image = models.ImageField(upload_to='looper', null=True, blank=True)
    bg_image = models.ImageField(upload_to='looper', null=True, blank=True)
    side =  models.CharField(max_length=50, null=True, blank=True, default="")

    def __str__(self) :

        return self.index + ' | ' + self.fk.name + ' | ' + self.title

@receiver(post_delete, sender=Looper_Component)
def submission_delete1(sender, instance, **kwargs) :
    instance.main_image.delete(False)
    instance.second_image.delete(False)
    instance.third_image.delete(False)
    instance.bg_image.delete(False)


class Informative_Section   (models.Model) :

    index = models.CharField(max_length=10, null=True, blank=True)
    page_name = models.CharField(max_length=100, null=True, blank=True)
    section_name = models.CharField(max_length=100, null=True, blank=True)
    sub_section_name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='informative', null=True, blank=True)
    second_image = models.ImageField(upload_to='informative', null=True, blank=True)
    third_image = models.ImageField(upload_to='informative', null=True, blank=True)
    bg_image = models.ImageField(upload_to='informative', null=True, blank=True)
    side =  models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) :

        return self.index + ' | ' + self.section_name + ' | ' + self.sub_section_name


@receiver(post_delete, sender=Informative_Section)
def submission_delete(sender, instance, **kwargs) :
    instance.main_image.delete(False)
    instance.second_image.delete(False)
    instance.third_image.delete(False)
    instance.bg_image.delete(False)


















