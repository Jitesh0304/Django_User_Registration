from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

class UserCreateForm(forms.ModelForm):
    password2 = forms.CharField(widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','password','password2']  # otp 
        labels = {'username':'Enter Your Full Name', 'email':'Enter Your Email'}
        help_text = {'username':'Enter Your full name'}
        error_messages ={'username':{'required':'You cannot leave this place as blank', 
                                 'max_length':'name should not exceed 20 charecters'}, 
                                 'password':{'required':'Password is necessary'}}
        widgets = {'password':forms.PasswordInput,
                   'password2':forms.PasswordInput,
                   'username':forms.TextInput(attrs={'class': 'css1 mycss2'}),}
        


class LoginOtpForm(forms.Form):
    email = forms.EmailField(label= "Your email", label_suffix=" ",
                             required=True, help_text="Enter your name")
    otp = forms.CharField(label= "Enter you 6 digit OTP", label_suffix=" ",
                          required=False,help_text="Enter your name")
    


# class CustomAuthenticationForm(AuthenticationForm):
#     email = forms.EmailField(label='Email')
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'] = self.fields.pop('email')


class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name']
        labels = {'email':'Email'}



class AdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = "__all__"
        labels = {'email':'Email'}


class ForgotPassForm(forms.Form):
    email = forms.EmailField()


class ResetPassForm(forms.Form):
    email = forms.EmailField()
    otp = forms.CharField()
    password1 = forms.CharField(widget= forms.PasswordInput)
    password2 = forms.CharField(widget= forms.PasswordInput)