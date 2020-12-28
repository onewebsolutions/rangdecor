from django.conf.urls import url, include
from contact import views


urlpatterns = [

    url(r"^panel/contact/$", views.contact_back, name="contact_back"),
    url(r"^panel/contact/add/$", views.contact_add, name="contact_add"),
    url(r"^panel/contact/edit/(?P<contact_pk>\d+)/$", views.contact_edit, name="contact_edit"),

    url(r"^panel/contact/lead/$", views.lead, name="lead"),
    url(r"^panel/contact/lead/view/(?P<lead_pk>\d+)/$", views.lead_view, name="lead_view"),
    url(r"^panel/contact/lead/revert/(?P<lead_pk>\d+)/$", views.lead_revert, name="lead_revert"),
    url(r"^panel/contact/lead/delete/(?P<lead_pk>\d+)/$", views.lead_delete, name="lead_delete"),


]
