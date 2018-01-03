from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from resume.views import ResumeView

urlpatterns = [
    url(r'^$', ResumeView.as_view(), name='resume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)