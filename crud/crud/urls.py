from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^mahasiswa/',include('mahasiswa.urls',namespace='mahasiswa')),
    url(r'^$', RedirectView.as_view(url='mahasiswa', permanent=False)),
    url(r'^admin/', admin.site.urls),
]
