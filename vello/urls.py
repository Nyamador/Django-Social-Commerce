from django.contrib import admin
from django.urls import path, include
from products import views as product_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('allauth.urls')),
    path('product/<slug:slug>', product_views.index , name='product-detail'),
]
