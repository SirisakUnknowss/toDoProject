from rest_framework import serializers
from rest_framework.exceptions import ValidationError
#Project
from .models import Task

class SlzTaskInput(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_name(self, value):
        if value is None:
            raise ValidationError('Please input name Task.')
        return value

class SlzTaskEditInput(SlzTaskInput):
    id = serializers.CharField()