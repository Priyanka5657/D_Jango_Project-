from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_contact = models.IntegerField()
    stu_pass = models.CharField(max_length=20)
    stu_cpass = models.CharField(max_length=20)
    # stu_image = models.FileField(upload_to='images/')
    stu_image = models.ImageField(upload_to='images/')

    stu_file = models.FileField(upload_to='resumes/')
