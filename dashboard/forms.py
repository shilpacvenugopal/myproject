## Creation of form for import data
from django import forms
from .models import Table2, Table1

class Table2ImportForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Table1.objects.all())

    class Meta:
        model = Table2
        fields = ('student', 'address', 'gender', 'age', 'blood_group')
