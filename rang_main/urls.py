from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^product/(?P<product_name>.*)/(?P<finish>.*)/$', views.product_tab, name='product_tab'),
    url(r'^product/(?P<product_name>.*)/$', views.product, name='product'),
    url(r'^gallery/(?P<pk>\d+)/$', views.gallery, name='gallery'),
    url(r'^catalogue/(?P<cata_name>.*)/$', views.catalogue, name='catalogue'),
    url(r'^contact/$', views.contact, name='contact'),

    url(r'^policy/privacy/$', views.policy_privacy, name='policy_privacy'),
    url(r'^policy/terms-of-service/$', views.policy_terms, name='policy_terms'),

    url(r'^search/$', views.search, name='search'),

]