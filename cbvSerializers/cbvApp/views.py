from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import generics,mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


#for making custom local Pagination class for some specific views
class StudentPagination(LimitOffsetPagination):
    page_size=3

#Viewset based views
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=LimitOffsetPagination
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['name','score'] #to make only these two fields avllble for ordering
    ordering=['id'] #by defauld o/p will be orderd by id
    # filter_backends=[filters.SearchFilter]
    # search_fields=['name','id']
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields=['name','score']
#generic based views-
class StudentList(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

"""""
#for using mixinsbased views-
mixin classes-ListModelMixin,CreateMM,RetrieveMM,UpdateMM,DestryMM
handler mthds-    get,           post,     get,       put,   delete
action methds-   list,           create, retrieve, update,    destroy

#Qsn--queryset, serializer_class are keywords?
we will extend mixins classes in StudentList class

class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
"""


"""# Class based views-.
class StudentList(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class StudentDetail(APIView):

    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        student=self.get_object(pk)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    def put(self,request,pk):
        student=self.get_object(pk)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        student=self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""