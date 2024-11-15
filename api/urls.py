from django.urls import path
from .views import *
urlpatterns = [
    path('submit/', submit_company_data, name='submit_company_data'),
    path('submit/<str:id>',company_data,name='company_data')
]

