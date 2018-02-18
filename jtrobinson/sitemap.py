from django.contrib.sitemaps import Sitemap
from portfolio.models import Project

class ProjectSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
