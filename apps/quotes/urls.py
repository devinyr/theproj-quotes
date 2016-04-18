from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from apps.quotes import views

urlpatterns = [
    url(r'^quotes/$', login_required(views.Dashboard.as_view(),login_url='/accounts/main'),name='quote-dashboard'),
    url(r'^create/$',login_required(views.QuoteView.as_view(),login_url='/accounts/main'),name='quote-create'),
    url(r'^add/(?P<id>\d+)$',login_required(views.add,login_url='/accounts/main'),name='quote-add'),
    url(r'^remove/(?P<id>\d+)$',login_required(views.remove,login_url='/accounts/main'),name='quote-remove'),
    url(r'^posts/(?P<id>\d+)$',login_required(views.UserPosts.as_view(),login_url='/accounts/main'),name='posts'),
]
