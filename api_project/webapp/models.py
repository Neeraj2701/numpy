from django.db import models


class employee(models.Model):
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	emp_Id=models.IntegerField()

	def __str__(self):
		return self.fname 


