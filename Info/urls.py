from django.urls import path
from .views import *

stu_urls=[
    path('index/',index,name='index'),
    path('register/',register,name='register'),
    path('details/',stu_details,name='details'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('edit/<int:id>/',user_edit),
    path('delete/<int:id>/',user_delete),
    #path('auth_registration/', user_registration),
    #path('auth_user/',auth_user),
    path('info/',queries),

]