from django.conf.urls import url
from django.contrib import admin

from .views import index, loginView, logoutView,profileView

urlpatterns = [
	url(r'^profile/$', profileView, name="profile"),
    url(r'^logout', logoutView, name="logout"),
	url(r'^login/$', loginView, name="login"),
    url(r'^$', index, name="index"),
    url(r'^admin/', admin.site.urls),
]
