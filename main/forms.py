from django import forms

from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name', 'group','lyceum', 'about', 'transport', 'vk', 'kxInt', 'kxDecimal', 'kyInt', 'kyDecimal')
