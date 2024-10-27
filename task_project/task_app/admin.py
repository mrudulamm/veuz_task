from django.contrib import admin
from . models import employee,CustomField, EmployeeCustomField
# Register your models here.
admin.site.register(employee)
admin.site.register(CustomField)
admin.site.register(EmployeeCustomField)