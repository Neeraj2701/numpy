from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from leaves.models import empleave
from leaves.serializers import empSerializer

# Create your views here.

@api_view(['GET','POST'])
def func(request):

	if request.method=='GET':
		emp1=empleave.objects.all()
		serializer=empSerializer(emp1,many=True)
		return Response(serializer.data)

	elif request.method=='POST':
		serializer=empSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)