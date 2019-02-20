from rest_framework import serializers
from classes.models import Classroom


class ClassroomListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
                'subject',
                'year',
                'teacher',     
                ]

class ClassroomDetailSerializers(serializers.ModelSerializer):
    class Meta:   
        model = Classroom
        fields = '__all__'


class ClassroomCreateUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
                'name',     
                'subject',
                'year',
                ]
