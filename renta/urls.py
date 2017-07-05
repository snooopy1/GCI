from django.conf.urls import url
from renta.views import index_renta

urlpatterns = [
    url(r'^$', index_renta),
]