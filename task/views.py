from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# Project
from .models import Task
from .serializers import SlzTaskInput, SlzTaskEditInput

# Create your views here.
class AddTask(GenericAPIView):
    queryset            = Task.objects.all()
    serializer_class    = SlzTaskInput

    def post(self, request, *args, **kwargs):
        serializerInput         = self.get_serializer(data=request.data)
        serializerInput.is_valid(raise_exception=True)
        equipment               = self.perform_create(serializerInput)
        serializerOutput        = self.get_serializer(equipment)
        return Response({"result":serializerOutput.data})
    
    def perform_create(self, serializer):
        validated = serializer.validated_data
        task = Task(
            name=validated['name'],
            detail=validated['detail'],
            dueDate=validated['dueDate']
        )
        task.save()
        return task

class EditTask(GenericAPIView):
    queryset            = Task.objects.all()
    serializer_class    = SlzTaskEditInput

    def post(self, request, *args, **kwargs):
        serializerInput = self.get_serializer(data=request.data)
        serializerInput.is_valid(raise_exception=True)
        task = Task.objects.filter(id=serializerInput.validated_data["id"])
        if not task.exists():
            return Response({"error":"task not found."}, status=status.HTTP_404_NOT_FOUND)
        task.update(
            name=serializerInput.validated_data["name"],
            detail=serializerInput.validated_data["detail"],
            completed=serializerInput.validated_data["completed"],
            dueDate=serializerInput.validated_data["dueDate"],
            )
        serializerOutput = self.get_serializer(task.first())
        return Response({"result":serializerOutput.data})
        
class RemoveTask(GenericAPIView):
    queryset            = Task.objects.all()
    serializer_class    = SlzTaskEditInput

    def post(self, request, *args, **kwargs):
        task = Task.objects.filter(id=request.POST["id"])
        if task.exists():
            task.delete()
            return Response({"result":"delete complete."})
        return Response({"error":"task not found."}, status=status.HTTP_404_NOT_FOUND)