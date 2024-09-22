
from django.contrib import admin
from django.urls import path
from flexipro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name="home" ),
    path('base/',views.base , name="base" ),
]
