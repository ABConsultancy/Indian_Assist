from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'IndianAssist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('Home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('Users.urls')),
]

admin.site.site_header = 'India Assist Admin'

