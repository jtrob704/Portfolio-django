from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from homepage.views import HomepageView

urlpatterns = [    
    url(r'^$', HomepageView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)