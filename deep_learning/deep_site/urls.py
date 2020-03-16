from django.conf.urls import url
from deep_site import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]
