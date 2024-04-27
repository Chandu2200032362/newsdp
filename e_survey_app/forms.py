# your_app/forms.py
from django import forms

from.models import  Feedback


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)



# survey_app/forms.py
from django import forms

class SurveyForm(forms.Form):
    question_text = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    answer = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))


class CustomerVerificationForm:
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    id_type = forms.ChoiceField(
        choices=[('passport', 'Passport'), ('driver_license', "Driver's License"), ('national_id', 'National ID')])
    id_number = forms.CharField(max_length=20)

    from django import forms

class FeedbackForm(forms.Form):
        name = forms.CharField(max_length=100)
        email = forms.EmailField()
        feedback = forms.CharField(widget=forms.Textarea)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise forms.ValidationError("Username must be at least 6 characters long.")

        return username

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']