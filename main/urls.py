from django.urls import path
from .views import *

urlpatterns=[
    path('',Index),
    path('contact/',Contact),
    path('project/',Project),
    path('sms/',SMS),
    path('detail/',Pdf6),
    path('detail/<pk>/', DepartmentDetail.as_view(), name='musician_details'),  
]