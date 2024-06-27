import logging
from rest_framework import serializers
from .models import Task, Label

logger = logging.getLogger(__name__)

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, required=False)
    parent_task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), required=False)
    subtasks = serializers.SerializerMethodField()



    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'parent_task', 'labels', 'created_at', 'updated_at', 'subtasks']
        read_only_fields = ['created_at', 'updated_at'] 

    def create(self, validated_data):
        try:
            labels_data = validated_data.pop('labels', [])
            parent_task_id = validated_data.pop('parent_task', None)
            task = Task.objects.create(**validated_data)
            for label_data in labels_data:
                label, _ = Label.objects.get_or_create(**label_data)
                task.labels.add(label)

            if parent_task_id:
                task.parent_task = parent_task_id
                task.save()

            return task
        except Exception as e:
            logger.error(f"Error creating task: {e}")
            raise serializers.ValidationError({"detail": "Error creating task"})

    def update(self, instance, validated_data):
        try:
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.status = validated_data.get('status', instance.status)

            parent_task = validated_data.get('parent_task', None)
            if parent_task is not None:
                instance.parent_task = parent_task

            labels_data = validated_data.pop('labels', None)
            if labels_data:
                instance.labels.clear()
                for label_data in labels_data:
                    label, _ = Label.objects.get_or_create(**label_data)
                    instance.labels.add(label)

            instance.save()
            return instance
        except Exception as e:
            logger.error(f"Error updating task: {e}")
            raise serializers.ValidationError({"detail": "Error updating task"})
        
    def get_subtasks(self, obj):
            subtasks = Task.objects.filter(parent_task=obj)
            
            if subtasks.exists():
                return TaskSerializer(subtasks, many=True).data
            else:
                return None
