from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_street, name='add_street'),
    path('street_list/', views.street_list, name='street_list'),
    path('street/<int:pk>/', views.street_detail, name='street_detail'),
    path('edit/<int:pk>/', views.edit_street, name='edit_street'),
    path('delete/<int:pk>/', views.delete_street, name='delete_street'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', views.search_street, name='search_street'),
    path('upload/', views.upload_file, name='upload_file'),
    path('export/csv/', views.export_streets_csv, name='export_streets_csv'),
    path('export/xlsx/', views.export_streets_xlsx, name='export_streets_xlsx'),
]
