from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import IndexView, DetailView, TagView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagView.as_view(), name='tagged'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
