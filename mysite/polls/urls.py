from django.conf.urls import url
from polls import views
from django.views.generic import DeleteView, ListView
from polls.models import Poll
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
]
