from django.db import models


class empleave(models.Model):
	ename=models.CharField(max_length=30)
	edesign=models.CharField(max_length=30)
	leave_bal=models.IntegerField()
	dt=models.DateField(auto_now=True)

	def __str__(self):
		return str (self.ename)


