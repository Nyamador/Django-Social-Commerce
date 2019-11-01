from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('allauth.urls')),
]
