from django.conf.urls import url, include
from authentication import views


urlpatterns = [

    url(r"^authentication/login/$", views.mylogin, name="mylogin"),
    url(r"^authentication/logout/$", views.mylogout, name="mylogout"),


]
