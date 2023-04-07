from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def student_list(request):
    if request.method=="GET":
        #in students var get all objects i.e. all students from db
        students=Student.objects.all()
        #create an object 'serializer' for StudentSerializer class (defnd in Serializer.py)
        #by passing all objects of Student class model  
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data) #this serialized data will go to http response
    elif request.method=="POST":
        #for posting a record in db, we will get that record through http  request-
        #below will deserialize the data and create object with enterd data
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():# to validiate if we giving data in correct format
            serializer.save()#to save the object in db
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE','PUT'])    
def student_detail(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    elif request.method=='PUT': #update
        serializer=StudentSerializer(student,data=request.data)#it wil ovride 'student' obj(pk) data with req.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


