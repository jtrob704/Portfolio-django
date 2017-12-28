from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from resume import views

urlpatterns = [
    url(r'^$', views.index, name='resume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)