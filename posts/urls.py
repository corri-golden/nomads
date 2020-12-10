from django.conf.urls import url

from . import views

app_name='posts'

urlpatterns = [
    url(r"^$", views.PostList.as_view(), name="all"),
    # url(r"post/in/(?P<slug>[-\w]+)/new/$", views.CreatePost.as_view(), name= "create"),
    # url(r"(?P<slug>[-\w]+)/(?P<pk>\d+)new/$", views.CreatePost.as_view(), name= "create"),
    # url(r"new/$", views.CreatePost.as_view(), name= "create"),
    # url(r'(?P<slug>[-\w]+)/create_post/$',views.CreatePost.as_view(),name='create_post'),
    # url(r'(?P<slug>[-\w]+)/new/$', views.CreatePost.as_view(), name= "create"),
    url(r'(?P<pk>\d+)/new/$', views.CreatePost.as_view(), name= "create"),
    



    url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
]


