from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


apps_patterns = [
    url(r'^professors/', include('professors.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^voting/', include('voting.urls')),
]

# General api patterns
urlpatterns = [
    url(r'^api/v1/', include(apps_patterns)),
]

# Add Documentation in URLS
if settings.DEBUG:
    from rest_framework_swagger.views import get_swagger_view  # NOQA

    schema_view = get_swagger_view(title='Education')

    urlpatterns += [
        url(r'^$', schema_view)
    ]
urlpatterns + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
