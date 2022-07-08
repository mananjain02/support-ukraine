from django.urls import path
from . import views

urlpatterns = [
    path('', views.LostAndFoundView.as_view(), name='lost_and_found'),
    path('report-missing', views.ReportMissingView.as_view(), name='report_missing')
]