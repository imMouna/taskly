from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm, LoginFrom, CreateTaskFrom, UpdateUserForm

from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Task

# - import Django messages (notification)
from django.contrib import messages


# Create your views here.


def home(request):
    
    return render(request, 'index.html')

# - Registering / Creating a user

def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "User registration was successful!")

            return redirect('my-login')

    context = {'form': form}

    return render(request, 'register.html', context=context)


# - Login a user

def myLogin(request):
    
    form = LoginFrom()

    if request.method == "POST":
        
        form = LoginFrom(request, request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                auth.login(request, user)
                
                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'my-login.html', context=context)


# - Dashboard Page 

@login_required(login_url='my-login')
def dashboard(request):
    
    return render(request, 'profile/dashboard.html')


# - Create a Task Page

@login_required(login_url='my-login')
def createTask(request):
    
    form = CreateTaskFrom()

    if request.method == 'POST':
        
        form = CreateTaskFrom(request.POST)
        
        if form.is_valid():
            
            task = form.save(commit=False)

            task.user = request.user
            
            task.save()
            
            return redirect('view-tasks')
    
    context = {'form': form}

    return render(request, 'profile/create-task.html', context=context)


# - View all tasks 
@login_required(login_url='my-login') 
def viewTasks(request):
    
    current_user = request.user.id
    
    task = Task.objects.all().filter(user=current_user)
    
    context = {'task': task}

    return render(request, 'profile/view-tasks.html', context=context)



# - Update task
@login_required(login_url='my-login') 
def updateTask(request, pk):
    
    task = Task.objects.get(id=pk)

    form = CreateTaskFrom(instance=task)

    if request.method == 'POST':
        
        form = CreateTaskFrom(request.POST, instance=task)
        
        if form.is_valid():
            
            form.save()

            return redirect('view-tasks')
    
    context = {'form': form}

    return render(request, 'profile/update-task.html', context=context)


# - Delete a Task
@login_required(login_url='my-login')
def deleteTask(request, pk):
    
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        
        task.delete()

        return redirect('view-tasks')

    return render(request, 'profile/delete-task.html')


# - Profile Management

@login_required(login_url='my-login')
def profile_management(request):
    
    if request.method == "POST":
        
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            
            user_form.save()

            return redirect('dashboard')
            
    
    user_form = UpdateUserForm(instance=request.user)
            
    context = {'user_form': user_form}
    
    return render(request, 'profile/profile-management.html', context=context)
    


# - Delete Account
@login_required(login_url='my-login')
def deleteAccount(request):
    
    if request.method == "POST":
        
        deleteUser = User.objects.get(username=request.user)
        
        deleteUser.delete()

        return redirect("")
    
    return render(request, 'profile/delete-account.html')
    
    
# - Logout a User

def userLogout(request):
    
    auth.logout(request)

    return redirect("")