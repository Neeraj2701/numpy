from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.models import employee
from webapp.serializers import employeeSerializer

class employeeList(APIView):


	def get(self,request):
		emp1=employee.objects.all()
		serializer=employeeSerializer(emp1,many=True)
		return Response(serializer.data)

	def post(self):
		pass

