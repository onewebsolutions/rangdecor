from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^panel/$', views.panel, name='panel'),
    url(r"^panel/page_handler/$", views.page_handler, name="page_handler"),
    url(r"^panel/page_handler_edit/(?P<page_name_w>.*)/$", views.page_handler_edit, name="page_handler_edit"),
    url(r"^panel/page_delete/(?P<page_name_w>.*)/$", views.page_delete, name="page_delete"),

    url(r"^panel/looper_section/$", views.looper_section, name="looper_section"),
    url(r"^panel/looper_section_add/$", views.looper_section_add, name="looper_section_add"),
    url(r"^panel/looper_section_edit/(?P<loop_sec_pk>\d+)/$", views.looper_section_edit, name="looper_section_edit"),
    url(r"^panel/looper_section_delete/(?P<loop_sec_pk>\d+)/$", views.looper_section_delete, name="looper_section_delete"),

    url(r"^panel/looper/(?P<loop_sec_name_w>.*)/looper_component/$", views.looper_component, name="looper_component"),
    url(r"^panel/looper/(?P<loop_sec_name_w>.*)/looper_component/add/$", views.looper_component_add, name="looper_component_add"),
    url(r"^panel/looper/(?P<loop_sec_name_w>.*)/looper_component/edit/(?P<loop_comp_pk>\d+)/$", views.looper_component_edit, name="looper_component_edit"),
    url(r"^panel/looper/(?P<loop_sec_name_w>.*)/looper_component/delete/(?P<loop_comp_pk>\d+)/$", views.looper_component_delete, name="looper_component_delete"),
    url(r"^panel/looper/(?P<img_path>.*)/looper_component/remove_image/(?P<img_name>.*)/(?P<loop_comp_pk>\d+)/$", views.remove_image_looper_component, name="remove_image_looper_component"),

    url(r"^panel/informative/informative_section/$", views.informative_section, name="informative_section"),
    url(r"^panel/informative/informative_section/add/$", views.informative_section_add, name="informative_section_add"),
    url(r"^panel/informative/informative_section/edit/(?P<pk>\d+)/$", views.informative_section_edit, name="informative_section_edit"),
    url(r"^panel/informative/informative_section/delete/(?P<pk>\d+)/$", views.informative_section_delete, name="informative_section_delete"),

    url(r"^panel/image/delete/(?P<img_path>.*)/(?P<img_name>.*)/(?P<pk>\d+)/$", views.remove_image, name="remove_image"),


]