from rest_framework import serializers
from .models import empleave

class empSerializer(serializers.ModelSerializer):
	class Meta:
		model=empleave
		fields='__all__'