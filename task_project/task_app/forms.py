from django import forms
from . models import employee, CustomField, EmployeeCustomField

class employeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'



class CustomFieldForm(forms.ModelForm):
    class Meta:
        model = CustomField
        fields = ['label', 'field_type']

class EmployeeCustomFieldForm(forms.ModelForm):
    class Meta:
        model = EmployeeCustomField
        fields = ['value']

    def __init__(self, *args, **kwargs):
        custom_fields = kwargs.pop('custom_fields', [])
        super().__init__(*args, **kwargs)
        for field in custom_fields:
            field_type = forms.CharField if field.field_type == 'text' else forms.IntegerField
            self.fields[f'custom_field_{field.id}'] = field_type(label=field.label, required=False)
