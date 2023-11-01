from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from registro_pago.models import Pago
from registro_pago.models import Reservas
from registro_pago.serializers import PagoSerializer, reservasSerializer
from .forms import añadirPago

@csrf_exempt
def pagoApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            pagos = Pago.objects.all()
            pagos_serializer = PagoSerializer(pagos, many=True)
            return JsonResponse(pagos_serializer.data, safe=False)
        else:
            pago = Pago.objects.get(id=id)
            pago_serializer = PagoSerializer(pago)
            return JsonResponse(pago_serializer.data, safe=False)

    elif request.method == 'POST':
        pago_data = JSONParser().parse(request)
        pago_serializer = PagoSerializer(data=pago_data)
        if pago_serializer.is_valid():
            pago_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        pago_data = JSONParser().parse(request)
        pago = Pago.objects.get(id=id)
        pago_serializer = PagoSerializer(pago, data=pago_data)
        if pago_serializer.is_valid():
            pago_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        pago = Pago.objects.get(id=id)
        pago.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    
    
    
@csrf_exempt
# reserva api
def reservasApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            reservas = Reservas.objects.all()
            reservas_serializer = reservasSerializer(reservas, many=True)
            return JsonResponse(reservas_serializer.data, safe=False)
        else:
            reserva = Reservas.objects.get(id=id)
            reserva_serializer = reservasSerializer(reserva)
            return JsonResponse(reserva_serializer.data, safe=False)

    elif request.method == 'POST':
        reserva_data = JSONParser().parse(request)
        reserva_serializer = reservasSerializer(data=reserva_data)
        if reserva_serializer.is_valid():
            reserva_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        reserva_data = JSONParser().parse(request)
        reserva = Reservas.objects.get(id=id)
        reserva_serializer = reservasSerializer(reserva, data=reserva_data)
        if reserva_serializer.is_valid():
            reserva_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        reserva = Reservas.objects.get(id=id)
        reserva.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    
    
    
    
def index(request):
    return render(request, 'app/index.html')


def pagoview(request):
    if request.method == 'POST':
        form = añadirPago(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = añadirPago()
    return render(request, 'añadirPagoForm.html', {'form': form})

