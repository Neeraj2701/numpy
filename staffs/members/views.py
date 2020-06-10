from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from members.models import empl
from members.serializers import emplserializer


@api_view(['GET','POST'])
def func(request):

	if request.method=='GET':
		emp1=empl.objects.all()
		serializer=emplserializer(emp1,many=True)
		return Response(serializer.data)

	elif request.method=='POST':
		serializer=emplserializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
