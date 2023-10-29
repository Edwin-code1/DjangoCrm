
from django.contrib.auth.models import Permission
from django.contrib.auth.permissions import BasePermission

class PatientPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_patient
    
    class DoctorPermission(BasePermission):
     def has_permission(self, request, view):
        return request.user.is_doctor