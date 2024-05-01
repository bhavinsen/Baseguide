from django.conf import settings
from django.urls import include, path
from django.contrib import admin
import logging

logger = logging.getLogger(__name__)

# from wagtail.admin import urls as wagtailadmin_urls
# from wagtail import urls as wagtail_urls
# from wagtail.documents import urls as wagtaildocs_urls

# from search import views as search_views
from django.views.generic import TemplateView

# import django_sso.sso_gateway.urls

urlpatterns = [
    path("", TemplateView.as_view(template_name="welcome.html")),
    path("django-admin/", admin.site.urls),
    # path("admin/", include(wagtailadmin_urls)),
    # path("documents/", include(wagtaildocs_urls)),
    # path("search/", search_views.search, name="search"),
    path("profile1/", include("user_profile.urls")),
    path("profile/", include("profiles.urls")),
    path("auth/", include("authentication.urls")),

    # Django SSO | https://pypi.org/project/django-sso/
    path('sso/', include('django_sso.sso_gateway.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def trigger_error(request):
    try:
        # Some code that might raise an exception
        1 / 0
    except Exception as e:
        # Log the exception
        logger.error('An error occurred: %s', str(e))
  
urlpatterns = urlpatterns + [
    path('sentry-debug/', trigger_error),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    # path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
