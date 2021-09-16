"""Post URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from posts import views

router = DefaultRouter()
router.register(r'delete', views.PostEditViewSet, basename='delete')
router.register(r'post', views.PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls))
]