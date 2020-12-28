from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('redirect.urls')),
    url(r'', include('rang_main.urls')),
    url(r'', include('panel.urls')),
    url(r'', include('product.urls')),
    url(r'', include('authentication.urls')),
    url(r'', include('contact.urls')),
    url(r'', include('vsg.urls')),
    url(r'', include('catalogue.urls')),
]

urlpatterns += static (
    settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static (
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)