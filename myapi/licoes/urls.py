from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LicaoViewSet

router = DefaultRouter()
router.register(r'licoes', LicaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
