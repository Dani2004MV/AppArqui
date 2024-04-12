from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservas.api.views import ClientViewSet, SedeViewSet, MesaViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'clientes', ClientViewSet)
router.register(r'sedes', SedeViewSet)
router.register(r'mesas', MesaViewSet)
router.register(r'reservas', ReservaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]