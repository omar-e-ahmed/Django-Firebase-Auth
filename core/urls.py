from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio_api.urls')),
    path('auth/', include('firebase_auth.urls')),
]
