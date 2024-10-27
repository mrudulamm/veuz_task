from django.urls import path
from . import views
urlpatterns = [
    path("",views.dashbord,name='dashboard'),
    path("createEmployee/",views.create_employee,name='createemployee'),
    path("search/",views.Search_Employee,name='search'),

    path('settings/', views.settings, name='settings'),
    path('add_custom_field/', views.add_custom_field, name='add_custom_field'),
    path('edit_employee/<int:pk>/', views.edit_employee, name='edit_employee'),

]