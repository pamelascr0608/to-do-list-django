from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
admin.site.site_header = u'Back office '
admin.site.index_title = u'Administração'
admin.site.site_title = u'Back office'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
