from django.urls import path
from .views import*

stu_urls=[
    path('grp/',StubranchAPI.as_view()),
    path('branch/<str:s>/', BranchAPI.as_view()),
    path('students/<int:id>/', StudentAPI.as_view()),
    path('students/', StudentAPI.as_view()),
    path('branch/<int:id>/',BranchAPI.as_view()),

]