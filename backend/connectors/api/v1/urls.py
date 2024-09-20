from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137058ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137058", Testconnectors137058ViewSet, basename="testconnectors137058"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
