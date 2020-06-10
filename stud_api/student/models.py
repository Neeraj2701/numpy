from django.db import models




class Stud(models.Model):
	Stud_ID=models.CharField(max_length=10)
	Stud_Name=models.CharField(max_length=20)
	Department=models.CharField(max_length=15)
	Marks=models.IntegerField()
	
	def __str__(self):
		return self.Stud_Name
