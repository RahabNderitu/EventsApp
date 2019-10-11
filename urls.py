from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('tables', views.tables, name='tables'),
    path('flot', views.flot, name='flot'),
    path('morris', views.morris, name='morris'),
    path('forms', views.forms, name='forms'),
    path('panels_wells', views.panels_wells, name='panels_wells'),
    path('buttons', views.buttons, name='buttons'),
    path('notifications', views.notifications, name='notifications'),
    path('typography', views.typography, name='typography'),
    path('icons', views.icons, name='icons'),
    path('grid', views.grid, name='grid'),
    path('blank', views.blank, name='blank'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),

    

]