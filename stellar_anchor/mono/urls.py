from django.conf.urls import patterns, url, include
from django.urls import path

# from mono.views import ProcessHookView


urlpatterns = []

if True:
    urlpatterns.append(path(r'^hook/$', ProcessHookView.as_view(), name='mono'),
    )
