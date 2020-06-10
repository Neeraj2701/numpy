from rest_framework import serializers
from .models import Stud

class StudSerializer(serializers.ModelSerializer):

	class Meta:
		model=Stud
		fields='__all__'

