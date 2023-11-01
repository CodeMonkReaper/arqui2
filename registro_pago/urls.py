from django.urls import path
from registro_pago import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pago/', views.pagoApi, name='pago-list'),  # Listar pagos y crear un nuevo pago
    path('pago/<int:id>/', views.pagoApi, name='pago-detail'),  # Ver detalles, actualizar y eliminar un pago
    path('reserva/', views.reservasApi, name='reserva-list'),  # Listar reservas y crear una nueva reserva
    path('reserva/<int:id>/', views.reservasApi, name='reserva-detail'),  # Ver detalles, actualizar y eliminar una reserva
    path('', views.index, name='index'),
    path('nuevopago/', views.pagoview, name='nuevoPago'),
]
