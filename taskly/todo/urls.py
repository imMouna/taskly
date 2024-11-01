from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    
    
    # ---------------------------- Homepage ----------------------------
    # -------------------------------------------------------------------------
    
    path('', views.home, name=""),
    

    # ---------------------------- Register a User ----------------------------
    # -------------------------------------------------------------------------
    
    path('register', views.register, name="register"),
    
    
    # ---------------------------- Login a User -------------------------------
    # -------------------------------------------------------------------------
    
    path('my-login/', views.myLogin, name="my-login"),
    
    
    # ---------------------------- Dashboard page ----------------------
    # -------------------------------------------------------------------------

    path('dashboard/', views.dashboard, name="dashboard"),
    
    
    # ---------------------------- CREATE TASK ------------------------------
    # -------------------------------------------------------------------------
    
    path('create-task/', views.createTask, name="create-task"),
    
    
    # ---------------------------- Read TASK ----------------------------------
    # -------------------------------------------------------------------------
    
    path('view-tasks/', views.viewTasks, name="view-tasks"),
    

    # ---------------------------- Update TASK ----------------------------------
    # ---------------------------------------------------------------------------
    
    path('update-task/<str:pk>/', views.updateTask, name="update-task"),
    
    
    # ---------------------------- Update TASK ----------------------------------
    # ---------------------------------------------------------------------------
    
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),
    
    
    # ---------------------------- Profile Management ----------------------------------
    # ---------------------------------------------------------------------------
    
    path('profile-management/', views.profile_management, name="profile-management"),
    
    
    # ---------------------------- Delete Account ----------------------------------
    # ------------------------------------------------------------------------------
    
    path('delete-account/', views.deleteAccount, name="delete-account"),

    # ---------------------------- Logout a User ------------------------------
    # -------------------------------------------------------------------------

    path('user-logout/', views.userLogout, name="user-logout"),
    
]