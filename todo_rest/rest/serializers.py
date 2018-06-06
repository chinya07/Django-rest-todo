from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


    def validate_title(self, value):
        if Task.objects.filter(title=value).exists():
            raise serializers.ValidationError('TITLE MUST BE UNIQUE!')
        return title