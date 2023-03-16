from django.contrib import admin
from django.urls import path, include
from api import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

urlpatterns = [
    path('', render, kwargs={
            'template_name': 'index.html',
        }, name='index'),    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', views.get_appeal, name='api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
