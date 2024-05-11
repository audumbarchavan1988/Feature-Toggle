"""
URL configuration for feature_toggle_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from feature_toggle.views import FeatureToggleViewSet, create_feature_toggle, activate_feature_toggle, deactivate_feature_toggle, get_all_feature_toggles, get_feature_toggle_details, update_feature_toggle_state, get_all_environments, get_all_applications

router = routers.DefaultRouter()
router.register(r'feature-toggles', FeatureToggleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('feature-toggles/', FeatureToggleViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('feature-toggles/create/', create_feature_toggle),
    path('feature-toggles/<int:toggle_id>/activate/', activate_feature_toggle),
    path('feature-toggles/<int:toggle_id>/deactivate/', deactivate_feature_toggle),
    path('feature-toggles/all/', get_all_feature_toggles),
    path('feature-toggles/<int:toggle_id>/', get_feature_toggle_details),
    path('feature-toggles/<int:toggle_id>/update-state/', update_feature_toggle_state),
    path('environments/', get_all_environments),
    path('applications/', get_all_applications),
]

