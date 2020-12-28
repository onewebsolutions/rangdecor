from django.conf.urls import url
from product import views

urlpatterns = [

    url(r"^panel/product/$", views.product_back, name="product_back"),
    url(r"^panel/product/add/$", views.product_add, name="product_add"),
    url(r"^panel/product/edit/(?P<product_pk>\d+)/$", views.product_edit, name="product_edit"),
    url(r"^panel/product/delete/(?P<product_pk>\d+)/$", views.product_delete, name="product_delete"),
    url(r"^panel/product/edit/remove_image/(?P<product_pk>\d+)/$", views.remove_image, name="remove_image"),

    url(r"^panel/product/sheet/(?P<product_pk>\d+)/$", views.sheet_back, name="sheet_back"),
    url(r"^panel/product/sheet/add/(?P<product_pk>\d+)/$", views.sheet_add, name="sheet_add"),
    url(r"^panel/product/sheet/edit/(?P<product_pk>\d+)/(?P<sheet_pk>\d+)/$", views.sheet_edit, name="sheet_edit"),
    url(r"^panel/product/sheet/delete/(?P<product_pk>\d+)/(?P<sheet_pk>\d+)/$", views.sheet_delete, name="sheet_delete"),


]