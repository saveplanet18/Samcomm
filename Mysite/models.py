from django.db import models

class Emp(models.Model):
    empid=models.IntegerField(default=0)
    empcode=models.TextField(max_length=50)
    empname=models.TextField(max_length=100)
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
    (Male, 'Male'),
    (FeMale, 'Female'),
    )
    dept_choice= [
        ('python', 'python'),
        ('php', 'php'),
        ('ruby', 'ruby'),
    ]
    hobbis_choice=(
        ('reading','reading'),
        ('writing','writing'),
        ('playing','playing'),
    )

    gender=models.CharField(max_length=50,choices=GENDER_CHOICES,blank=False,null=False,default=Male)
    dept=models.CharField(max_length=30,choices=dept_choice,blank=False,null=False,default='python')
    hobbis=models.CharField(max_length=50,choices=hobbis_choice,blank=False,null=False,default='reading')
    photo=models.FileField(upload_to='uploads/% Y/% m/% d/')

    def __str__(self):
        return self.empname

