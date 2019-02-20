from django.shortcuts import render
from rest_framework.generics import  ListAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView,CreateAPIView
from classes.models import Classroom
from .serializers import ClassroomListSerializers, ClassroomDetailSerializers,ClassroomCreateUpdateSerializers

# Create your views here.
class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializers



class ClassroomDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomCreateUpdateSerializers
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomCreateView(CreateAPIView):
    serializer_class = ClassroomCreateUpdateSerializers
    
    def perform_create(self,serializer):
        serializer.save(teacher=self.request.user)
