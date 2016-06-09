from django.conf.urls import url
from django.contrib import admin
from search import views as search_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(regex=r'^navigator/', view=search_views.request),
]
