from rest_framework import viewsets
from reservas.models import Cliente, Mesa, Sede, Reserva
from reservas.api.serializers import ClientSerializer, SedeSerializer, MesaSerializer, ReservaSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Cliente."""
    queryset = Cliente.objects.all()
    serializer_class = ClientSerializer

class MesaViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Mesa."""
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class SedeViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Sede."""
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Reserva."""
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer