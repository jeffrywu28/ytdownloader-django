from django.urls import path
from . import views

urlpatterns = [
    path('', views.yt_download,name='home'),
    path('download/',views.download),
    path('download_complete/<res>',views.download_complete,name='download_complete')
] 