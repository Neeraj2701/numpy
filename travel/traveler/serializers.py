from rest_framework import serializers
from .models import tour

class tourSerializer(serializers.ModelSerializer):
	class Meta:
		model=tour
		fields='__all__'


