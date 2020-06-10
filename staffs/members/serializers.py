from rest_framework import serializers
from .models import empl

class emplserializer(serializers.ModelSerializer):
	class Meta:
		model=empl
		fields='__all__'
