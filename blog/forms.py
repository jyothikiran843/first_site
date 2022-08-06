from dataclasses import fields
from pyexpat import model
from blog.models import Article
from django import forms

class ArticleInput(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','content','active']