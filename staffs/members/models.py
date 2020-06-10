from django.db import models


class empl(models.Model):
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	city=models.CharField(max_length=30)
	salary=models.CharField(max_length=7)
	create_dt=models.DateField(auto_now=True)

	def __str__(self):
		return str(self.name)

