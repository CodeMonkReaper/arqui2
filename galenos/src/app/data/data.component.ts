import { Component, OnInit } from '@angular/core';
import{ RestService } from '../services/rest.service'
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})
export class DataComponent implements OnInit {

  registros: any[] = [];

  constructor(private servicio: RestService) {}

  ngOnInit() {
    this.servicio.obtenerRegistros().subscribe((data: any) => {
      this.registros = data as any[];
      console.log(this.registros)
    });
  }

  agregarRegistro(nuevoRegistro: any) {
    this.servicio.agregarRegistro(nuevoRegistro).subscribe((data: any) => {
      this.registros.push(data);
    });
  }

  actualizarRegistro(id:any, datosActualizados: any) {
    this.servicio.actualizarRegistro(id, datosActualizados).subscribe(() => {
      // Realiza alguna acción después de actualizar
    });
  }

  eliminarRegistro(id: any) {
    this.servicio.eliminarRegistro(id).subscribe(() => {
      this.registros = this.registros.filter(registro => registro._id !== id);
    });
  }

}
