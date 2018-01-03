from django.conf.urls import url
from . import views

app_name = 'kof'

urlpatterns = [
    url(r'^$', views.fighters, name='fighters'),
    # url(r'^filter', views.fighters_filter, name='fighters_filter'),
]
