"""
URLconf for development-only views.
This gets imported by urls.py and added to its URLconf if we are running in
development mode; otherwise, it is ignored.
"""


from cms.djangoapps.contentstore.views.dev import dev_mode
from django.urls import path

urlpatterns = [
    path('dev_mode', dev_mode, name='dev_mode'),
]
