from django.db import models


class tour(models.Model):
	name=models.CharField(max_length=20)
	family=models.IntegerField()
	contact=models.CharField(max_length=15)
	arrival=models.CharField(max_length=30)
	depart=models.CharField(max_length=30)
	total=models.IntegerField()

	def __str__(self):
		return str(self.name)