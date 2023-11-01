from rest_framework import serializers
from .models import Pago, Reservas

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ('id','cliente','cantidad','rutCliente','fecha','descripcion')


class reservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = ('id','cliente','rutCliente','fecha','hora','medico','especialidad','motivoConsulta')