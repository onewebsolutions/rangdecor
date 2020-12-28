from django.conf.urls import url, include
from vsg import views


urlpatterns = [

    url(r"^visual-gallery/(?P<vsg_area>.*)/$", views.vsg, name="vsg"),
    url(r"^panel/vsg_back/$", views.vsg_back, name="vsg_back"),
    url(r"^panel/vsg_back_edit/(?P<vsg_pk>\d+)/$", views.vsg_back_edit, name="vsg_back_edit"),
    url(r"^panel/vsg_back_delete/(?P<vsg_pk>\d+)/$", views.vsg_back_delete, name="vsg_back_delete"),


]
