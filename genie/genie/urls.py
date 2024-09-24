
from django.contrib import admin
from django.conf import settings
from django.urls import path
from geniedocs import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base , name="base"),
    path('', views.home , name="home"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)