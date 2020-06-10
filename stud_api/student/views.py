from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from student.models import Stud
from student.serializers import StudSerializer


@api_view(['GET','POST'])
def get(request):

	if request.method=='GET':
		stud1=Stud.objects.all()
		serializer=StudSerializer(stud1,many=True)
		return Response(serializer.data)

	elif request.method=='POST':
		serializer=StudSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
