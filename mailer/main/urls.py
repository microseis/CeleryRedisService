from django.conf.urls import url
from .views import ContactView
from . import views
from .views import SendTemplateMailView , GetDataView, ImageView
urlpatterns = [
    url(r'^$',  ContactView.as_view(), name='contact'),
    url(r'^image_load/(?P<slug>[0-9A-Fa-f]{8}(-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12})/$', ImageView.as_view()),
    url(r'^data/(?P<pk>\d+)/$', GetDataView.as_view()),
    url(r'^send$', SendTemplateMailView.as_view(), name='send'),
    url(r'^subscribed$',  views.subscribed, name='subscribed'),
    url(r'^sendbulk', views.sendbulk, name='sendbulk'),
]
