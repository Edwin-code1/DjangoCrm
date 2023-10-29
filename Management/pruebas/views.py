from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django import request  # Corrected the import statement
from django.contrib.auth.decorators import permission_required

from .forms import TreatmentForm, PatientForm, AppointmentForm, RegistrationForm
from .models import Treatment, Patient


def index(request):
    return render(request, 'pruebas/index.html')

def add_treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Treatment added successfully.')
            return redirect('patient_list')
    else:
        form = TreatmentForm()

    context = {'form': form}
    return render(request, 'pruebas/add_treatment.html', context)

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    context = {
        'form': form,
    }
    return render(request, 'patient_add.html', context)


def add_appointment(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            return redirect('patient_list')  # You can change the URL name to match your project's URL configuration
    else:
        form = AppointmentForm()

    context = {
        'form': form,
        'patient': patient,
    }
    return render(request, 'appointment_add.html', context)

def patient_list(request):
    patients = Patient.objects.all()

    context = {
        'patients': patients,
    }
    return render(request, 'patient_list.html', context)

@permission_required('patient')
def appointment_scheduler(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment added successfully.')
            return redirect('patient_list')
    else:
        form = AppointmentForm()

    context = {'form': form}
    return render(request, 'pruebas/appointment_scheduler.html', context)

def is_doctor(request):
    return request.user.groups.filter(name='Doctor').exists()

@permission_required('doctor')
def doctor_module(request):
    pass

def index(request):
    if is_doctor(request):
        # Display the doctor navigation menu
        pass
    else:
        # Display the patient navigation menu
        pass
        # Display the patient navigation menu


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Create a new user account
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )

            # Assign the user to the appropriate group based on their user type
            if form.cleaned_data['user_type'] == 'doctor':
                user.groups.add(Group.objects.get(name='Doctor'))
            else:
                user.groups.add(Group.objects.get(name='Patient'))

            # Login the user
            auth.login(request, user)

            # Redirect the user to the appropriate page
            if is_doctor(request):
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')

        else:
            # Registration failed
            return render(request, 'registration.html', {'form': form})

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})

@permission_required('doctor')
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

@permission_required('patient')
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')
        
    def login(request):
          if request.method == 'POST':
        # Authenticate the user
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

          if user is not None:
            # Login the user
            auth.login(request, user)

            # Redirect the user to the appropriate page
            if is_doctor(request):
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
          else:
            # Login failed
            return render(request, 'login.html', {'error': 'Invalid username or password'})
        
@permission_required('doctor')
def doctor_dashboard(request):
    pass

@permission_required('patient')
def patient_dashboard(request):
    pass

'''

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Create a new user account
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )

            # Assign the user to the appropriate group based on their user type
            if form.cleaned_data['user_type'] == 'doctor':
                user.groups.add(Group.objects.get(name='Doctor'))
            else:
                user.groups.add(Group.objects.get(name='Patient'))

            # Login the user
            auth.login(request, user)

            # Redirect the user to the appropriate page
            if is_doctor(request):
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')

        else:
            # Registration failed
            return render(request, 'registration.html', {'form': form})
        '''

