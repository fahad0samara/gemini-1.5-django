

# Add an empty line here

# Add a comment to clarify the import
# Import the 'path' function from 'django.urls'
# PaLM2/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('generate-text/', views.text_form, name='text_form'),
    path('generate-text-only/', views.generate_text_only, name='generate_text_only'),
]
