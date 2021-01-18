from django.urls import path

from imageupload import views

urlpatetrns = [
    path('', views.home, name='home'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('filelist/', views.imagelist, name='imagelist'),
    path('')
]