from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=100,blank=True)
    gpa=models.DecimalField(max_digits=4,decimal_places=2)
    email=models.EmailField(max_length=100)
    human=models.BooleanField(blank=True,default=False)
    slug=models.SlugField(blank=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.sname)
        super(Student,self).save()

    def __str__(self):
        return self.sname

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.slug)])