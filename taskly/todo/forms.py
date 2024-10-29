from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput   
from django import forms
from .models import Task




# Register a User      

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

# login a User

class LoginFrom(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


#- Create a task

class CreateTaskFrom(forms.ModelForm):

    class Meta:
        
        model = Task
        fields = ['title', 'content',]
        exclude = ['user',]
        
        
# - Update a user

class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email',]
        exclude = ['password1', 'password2',]





