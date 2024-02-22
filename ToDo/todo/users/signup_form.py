from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email= forms.EmailField(max_length=100, help_text='Enter email')
    class Meta:
        model = User
    
        fields = ('username','email','password1','password2')
        labels = {
            'username':'Username',
            'email':'Email',
            'password1':'Password',
            'password2':'Confirm Password'
        }
        help_texts={
            'username':'Enter username',
            'email':'Enter email',
            'password1':'Enter password',
            'password2':'Enter Password'
        }
    
    # error_messages={
    #     'username':'Username required',
    #     'email':'Email required',
    #     'passw'

    # }