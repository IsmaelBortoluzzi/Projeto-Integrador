"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('client/', include('client.urls')),
    path('brand/', include('product_brand.urls')),
    path('supplier/', include('supplier.urls')),
    path('product/', include('product.urls')),
    path('bills-tobe-paid/', include('bills_tobe_paid.urls')),
    path('entry-document/', include('product_entry_document.urls')),
    path('entry-product/', include('product_entry_product.urls')),
    path('bills-tobe-received/', include('bills_tobe_received.urls')),
    path('order/', include('order.urls')),
    path('product-output/', include('product_output.urls')),
    path('grill-reserve/', include('grill_reserve.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
