from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'website.views.index', name="index"),
    url(r'^(?P<oid>[-A-Za-z0-9_]+)$', 'website.views.one_word', name="one_word"),
]
