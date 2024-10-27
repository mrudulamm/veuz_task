from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import employeeForm
from django.db.models import Q
from .models import employee, CustomField, EmployeeCustomField
from .forms import CustomFieldForm, EmployeeCustomFieldForm
def dashbord(request):
    employees = employee.objects.all()
    return render(request,'dashboard.html',{'employees':employees})
def create_employee(request):
    employees = employee.objects.all()
    if request.method=='POST':
        form=employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form=employeeForm()
    return render(request,'index.html',{'form':form,'employees':employees})

def Search_Employee(request):
    query=None
    employees=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        employees=employee.objects.filter(Q(name__icontains=query))
    else:
        employees=[]
    context={'employees':employees,'query':query}
    return render(request,'search.html',context)

@login_required
def settings(request):
    custom_fields = CustomField.objects.all()
    return render(request, 'settings.html', {'custom_fields': custom_fields})

@login_required
def add_custom_field(request):
    if request.method == 'POST':
        form = CustomFieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = CustomFieldForm()
    return render(request, 'add_custom_field.html', {'form': form})

@login_required
def edit_employee(request, pk):
    employeee = employee.objects.get(pk=pk)
    custom_fields = CustomField.objects.all()
    if request.method == 'POST':
        for field in custom_fields:
            value = request.POST.get(f'custom_field_{field.id}')
            custom_value, created = EmployeeCustomField.objects.get_or_create(
                employeee=employeee, custom_field=field
            )
            custom_value.value = value
            custom_value.save()
        return redirect('dashboard')
    return render(request, 'edit_employee.html', {
        'employeee': employeee,
        'custom_fields': custom_fields,
        'employee_custom_fields': EmployeeCustomField.objects.filter(employeee=employeee),
    })
