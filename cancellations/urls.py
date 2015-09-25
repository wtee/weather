from django.conf.urls import url
from cancellations import views
from django.contrib.admin.sites import AdminSite

urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^cancellations/$', views.IndexView.as_view(), name='index'),
  url(r'^cancellations/?P(<pk>)[0-9]+/$', views.DetailView.as_view(), name='event'),
]

AdminSite.site_header = "Cancellations administration"
AdminSite.site_title = "Cancellations administration"
