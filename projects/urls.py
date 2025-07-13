# mypersonalportfolio/projects/urls.py

from django.urls import path
from . import views # We'll create these views later

app_name = 'projects' # Namespace for this app's URLs

urlpatterns = [
    # Example: A URL for listing all projects
    # path('', views.ProjectListView.as_view(), name='list'),
    # Example: A URL for viewing a single project by slug
    # path('<slug:slug>/', views.ProjectDetailView.as_view(), name='detail'),
]