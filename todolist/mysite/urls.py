"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist.urls')),
]

# ______________________________________________________________________________
#                                                                              
#  This code defines the URL patterns for the Django project. It includes two  
#  main patterns: one for the Django admin interface and another for the       
#  'todolist' app's URLs.                                                     
#                                                                              
#  - The first path() function maps the '/admin/' endpoint to the Django admin 
#    interface. This allows administrators to manage the site's data through   
#    the admin interface.                                                      
#                                                                              
#  - The second path() function maps the '/todolist/' endpoint to the URL      
#    patterns defined in the 'todolist' app's urlpatterns. It includes the    
#    URLs specified in the 'todolist.urls' module, allowing clients to access  
#    the API endpoints and views defined in the 'todolist' app.                
#                                                                              
#  This configuration separates the admin interface from the application's     
#  API endpoints, providing a clean and organized URL structure. Clients can   
#  access both the admin interface and the task-related API endpoints through  
#  their respective URLs.                                                      
#                                                                              
# ______________________________________________________________________________
