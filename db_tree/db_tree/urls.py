from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.

import db_too_tree.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(db_too_tree.urls))
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
