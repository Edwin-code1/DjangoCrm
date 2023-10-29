
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_treatment/', views.add_treatment, name='add_treatment'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_appointment/<int:patient_id>/', views.add_appointment, name='add_appointment'),
    path('patient_list/', views.patient_list, name='patient_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard', permission_required='doctor'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard', permission_required='patient'),
    # Add more URL patterns as needed
]
