#from django.http import JsonResponse
#from django.shortcuts import render
from api.models import student
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET','POST'])
def students(request):
    if request.method == 'GET':        
        students = student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def student_detail(request, pk):
    try:        
        Student_id = student.objects.get(pk=pk)
    except  student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(Student_id) 
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(Student_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Student_id.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)