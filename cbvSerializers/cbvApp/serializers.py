from rest_framework import serializers
from cbvApp.models import Student

#here we are use drf property Modelserializer
class StudentSerializer(serializers.ModelSerializer):
    #meta class will extend Model which is to be serialized
    class Meta:
        model=Student
        fields=['id','name','score']
