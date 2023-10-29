from django import forms

from .models import Treatment,Patient,Appointment

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['name', 'description', 'cost']



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient  # Specify the model to use
        fields = ['name', 'age', 'gender']  # Define the fields to include in the form

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['date', 'time', 'doctor']

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=(('patient', 'Patient'), ('doctor', 'Doctor')))

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError("Passwords must match.")

        return password2