"""jobiewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import core.views as coreviews
urlpatterns = [
    path('', coreviews.HomeView.as_view(), name='home'),
    path('project/<int:project_id>', coreviews.ProjectView.as_view(), name='project'),
    path('project/image/<int:projectimage_id>', coreviews.Project_Image_Download.as_view(), name='project-mage-download'),
    
]
