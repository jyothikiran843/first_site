from multiprocessing.sharedctypes import Value
from xml.dom import ValidationErr
from django import forms

class Student_Create(forms.Form):
    sname=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=100)
    gpa=forms.DecimalField(decimal_places=2,max_digits=4)
    human=forms.BooleanField(widget=forms.CheckboxInput(),required=False)