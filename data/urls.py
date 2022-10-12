from django.urls import path 
from data.views import DepartmentClass,PostMetod,PutMetod

urlpatterns = [ 
    path('GetDepartments',DepartmentClass.GetDepartment, name='GetDepartment'),   
    path('CreateDepartment',PostMetod.as_view(), name='CreateDepartment'),  
    path('GetDepartmentByID/<int:id>',DepartmentClass.GetDepartmentByID, name='GetDepartmentByID'),   
    path('UpdateDepartment/<int:id>',PutMetod.as_view(),name='UpdateDepartment'),   
    path('DeleteDepartment/<int:id>',DepartmentClass.DeleteDepartment,name='DeleteDepartment'),   
]