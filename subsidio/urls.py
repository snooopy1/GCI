from django.conf.urls import url
from subsidio.views import index

urlpatterns = [
    url(r'^$', index),
]