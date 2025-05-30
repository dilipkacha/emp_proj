from django.db import models

# Create your models here.
class emp(models.Model):
    emp_nm=models.CharField(max_length=100)
    dep=models.CharField(max_length=100)
    salary=models.IntegerField()
    
