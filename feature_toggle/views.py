from django.shortcuts import render
from rest_framework import viewsets
from .models import FeatureToggle, Environment, Application
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FeatureToggleSerializer, FeatureToggleCreateSerializer, EnvironmentSerializer, ApplicationSerializer

class FeatureToggleViewSet(viewsets.ModelViewSet):
    queryset = FeatureToggle.objects.all()
    serializer_class = FeatureToggleSerializer

@api_view(['POST'])
def create_feature_toggle(request):
    if request.method == 'POST':
        serializer = FeatureToggleCreateSerializer(data=request.data)
        if serializer.is_valid():
            toggle = FeatureToggle.objects.create(
                name=serializer.validated_data['name'],
                description=serializer.validated_data['description'],
                enabled=serializer.validated_data['enabled']
            )
            toggle_serializer = FeatureToggleSerializer(toggle)
            return Response(toggle_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def activate_feature_toggle(request, toggle_id):
    try:
        toggle = FeatureToggle.objects.get(pk=toggle_id)
    except FeatureToggle.DoesNotExist:
        return Response({'error': 'Feature toggle not found'}, status=status.HTTP_404_NOT_FOUND)

    toggle.enabled = True
    toggle.save()
    toggle_serializer = FeatureToggleSerializer(toggle)
    return Response(toggle_serializer.data)

@api_view(['POST'])
def deactivate_feature_toggle(request, toggle_id):
    try:
        toggle = FeatureToggle.objects.get(pk=toggle_id)
    except FeatureToggle.DoesNotExist:
        return Response({'error': 'Feature toggle not found'}, status=status.HTTP_404_NOT_FOUND)

    toggle.enabled = False
    toggle.save()
    toggle_serializer = FeatureToggleSerializer(toggle)
    return Response(toggle_serializer.data)


@api_view(['GET'])
def get_all_feature_toggles(request):
    toggles = FeatureToggle.objects.all()
    serializer = FeatureToggleSerializer(toggles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_feature_toggle_details(request, toggle_id):
    try:
        toggle = FeatureToggle.objects.get(pk=toggle_id)
    except FeatureToggle.DoesNotExist:
        return Response({'error': 'Feature toggle not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = FeatureToggleSerializer(toggle)
    return Response(serializer.data)


@api_view(['POST'])
def update_feature_toggle_state(request, toggle_id):
    try:
        toggle = FeatureToggle.objects.get(pk=toggle_id)
    except FeatureToggle.DoesNotExist:
        return Response({'error': 'Feature toggle not found'}, status=status.HTTP_404_NOT_FOUND)
  
    toggle.enabled = not toggle.enabled
    toggle.save()
    toggle_serializer = FeatureToggleSerializer(toggle)
    return Response(toggle_serializer.data)


@api_view(['GET'])
def get_all_environments(request):
    environments = Environment.objects.all()
    serializer = EnvironmentSerializer(environments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_applications(request):
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)


