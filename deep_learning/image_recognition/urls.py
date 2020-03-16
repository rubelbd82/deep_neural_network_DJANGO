from django.conf.urls import url
from image_recognition import views


urlpatterns = [
    url(r'^$', views.index,  name="image_recognition"),
    url(r'^fer/$', views.fer, name="fer"),
    url(r'^recognize/$', views.recognize, name="recognize"),
]
