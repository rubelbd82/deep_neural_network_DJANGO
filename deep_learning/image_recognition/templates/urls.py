from django.conf.urls import url
from deep_site import views

urlpatterns = [
    url(r'^image_recognition$', views.index, name="index"),
]
