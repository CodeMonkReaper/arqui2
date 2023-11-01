import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RestService {
  private apiURL = 'http://127.0.0.1:5000'; // Reemplaza con la URL de tu servidor Flask

  constructor(private http: HttpClient) {}

  // Define métodos para realizar solicitudes HTTP, por ejemplo:

  obtenerRegistros() {
    return this.http.get(`${this.apiURL}/api/registro_pago_reserva`);
  }

  agregarRegistro(nuevoRegistro: any) {
    return this.http.post(`${this.apiURL}/api/registro_pago_reserva`, nuevoRegistro);
  }

  actualizarRegistro(id:any, datosActualizados: any) {
    return this.http.put(`${this.apiURL}/api/registro_pago_reserva/${id}`, datosActualizados);
  }

  eliminarRegistro(id:any) {
    return this.http.delete(`${this.apiURL}/api/registro_pago_reserva/${id}`);
  }
}
