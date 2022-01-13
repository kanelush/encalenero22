from django.urls import path
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, NegocioSitemap, CategorySitemap


sitemaps = {  'StaticViewSitemap': StaticViewSitemap, 'NegocioSitemap':NegocioSitemap, 'CategorySitemap':CategorySitemap}
from . import views
from .views import NegocioDetailView

urlpatterns = [
    path('', views.base, name="base"),
    path('categoria/<int:category_id>', views.list, name="list"),
    path('<slug:slug>', NegocioDetailView.as_view(), name='detail'),
    path('contacto/', views.contact, name="contact"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
