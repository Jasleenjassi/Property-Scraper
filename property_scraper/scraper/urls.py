from django.contrib import admin
from django.urls import path, include
from scraper.views import scrape_property_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scrape_property_view, name='scrape_property'),
    path('search/', scrape_property_view, name='scrape_property'),  # Add this line
]