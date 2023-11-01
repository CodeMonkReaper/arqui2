from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from  bson import json_util ,ObjectId # Importa json_util para convertir ObjectId
from flask_cors import CORS  # Importa CORS


app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb+srv://codemark:123panadero@clusterhospital.5lp8kit.mongodb.net/')
db = client['pagos']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/registro_pago_reserva', methods=['GET'])
def get_registro_pago_reserva():
    pagos = list(db.registro_pago_reservas.find())
    
    # Convierte los ObjectId a cadenas de texto utilizando json_util
    json_data = json_util.dumps(pagos)
    
    return jsonify(json_data)

@app.route('/api/registro_pago_reserva', methods=['POST'])
def new_reserva():
    
    data=request.json()
    if data is None or 'cliente' not in data or 'rutCliente' not in data or 'fecha' not in data or 'hora' not in data or 'medico' not in data or 'especialidad' not in data or 'motivoConsulta' not in data:
        return jsonify({'error': 'Datos no válidos o faltantes'}), 400
    db.registro_pago_reservas.insert_one(data)
        
@app.route('/api/registro_pago_reserva/<id>', methods=['DELETE'])
def delete_reserva(id):
    obj_id=ObjectId(id)
    result=db.registro_pago_reservas.delete_one({'_id':obj_id})
    if result.deleted_count>0:
        return jsonify({'message':'Reserva eliminada correctamente'})
    else:
        return jsonify({'message':'No se pudo eliminar la reserva'})
@app.route('/api/registro_pago_reserva/<id>', methods=['PUT'])
def update_reserva(id):
    data=request.json()
    if data is None or not any(key in data for key in['cliente','rutCliente','fecha','hora','medico','especialidad','motivoConsulta']):
        return jsonify({'error':'Datos no válidos o faltantes'}),400
    result=db.registro_pago_reservas.update_one({'_id':ObjectId(id)},{'$set':data})




if __name__ == '__main__':
    app.run(debug=True)

