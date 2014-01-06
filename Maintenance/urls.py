from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Maintenance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='500.html'), name='maintenance'),
)
handler400 = "TemplateView.as_view(template_name='500.html')"
handler404 = "TemplateView.as_view(template_name='500.html')"
