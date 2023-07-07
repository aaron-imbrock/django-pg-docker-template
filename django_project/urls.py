from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path("login/", admin.site.urls),
    # Local apps
    path("", include("pages.urls")),
    path("books/", include("books.urls")),  # new
]

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns