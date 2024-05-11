from rest_framework import serializers
from .models import FeatureToggle, Environment, Application

class FeatureToggleCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    enabled = serializers.BooleanField(default=False)

class FeatureToggleSerializer(serializers.ModelSerializer):
    environment_name = serializers.SerializerMethodField()
    application_name = serializers.SerializerMethodField()
    owner = serializers.CharField(max_length=100, required=False)
    creation_date = serializers.DateTimeField(read_only=True)
    last_modified_date = serializers.DateTimeField(read_only=True)
    notes = serializers.CharField(max_length=1000, required=False)

    class Meta:
        model = FeatureToggle
        fields = ['id', 'name', 'description', 'enabled', 'is_global', 'environment', 'environment_name', 'application', 'application_name', 'owner', 'creation_date', 'last_modified_date', 'notes']
        read_only_fields = ['id', 'creation_date', 'last_modified_date']

    def get_environment_name(self, obj):
        if obj.environment:
            return obj.environment.name
        return None

    def get_application_name(self, obj):
        if obj.application:
            return obj.application.name
        return None

class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ['id', 'name']
        read_only_fields = ['id']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name']
        read_only_fields = ['id']

