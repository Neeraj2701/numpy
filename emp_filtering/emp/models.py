from django.db import models

# Create your models here.

class employee(models.Model):
	emp_id=models.CharField(max_length=10)
	fname=models.CharField(max_length=30)
	lname=models.CharField(max_length=30)
	contact=models.IntegerField()
	emp_email=models.EmailField()
	join_dt=models.DateField()
	feedback=models.TextField()

	def __str__(self):
		return self.fname 
