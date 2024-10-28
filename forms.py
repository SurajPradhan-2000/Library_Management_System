from django import forms
from django.contrib.auth.models import User
from . models import IssuedBook
from .models import Book
from .models import Students

class IssueBookForm(forms.ModelForm):
    isbn2 = forms.ModelChoiceField(queryset=Book.objects.all(), label="Book ISBN")
    name2 = forms.ModelChoiceField(queryset=Students.objects.all(), label="Student Details")

    class Meta:
        model = IssuedBook
        fields = ['isbn2', 'name2', 'expiry_date']