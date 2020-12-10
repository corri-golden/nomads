from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^$',views.ListGroups.as_view(),name='all'),
    path(r'^new/$',views.CreateGroup.as_view(),name='create'),
    # url(r'posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
    # url(r'(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
    url(r'(?P<pk>\d+)/$',views.SingleGroup.as_view(),name='single'),

    


    


]
