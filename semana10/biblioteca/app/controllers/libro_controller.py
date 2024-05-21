#ruta para libro especifico por id
from flask import Blueprint, request, jsonify
from models.libro_model import Libro
from views.libro_view import render_libro_list, render_libro_detail

# Crear un blueprint para el controlador de animales
libro_bp = Blueprint("libro", __name__)

#ruta para mostrar un libro por id
@libro_bp.route("/libros/<int:id>", methods=["GET"])
def get_libro(id):
    libro=Libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error":"Libro no encontrado"}),404

#ruta para crear un nuevo libro
@libro_bp.route("/libros", methods=["POST"])
def create_libro():
    data= request.json
    titulo=data.get("titulo")
    autor= data.get("autor")
    edicion = data.get("edicion")
    disponibilidad= data.get("disponibilidad")
    
    #validacion simple de datos de entrada
    if not titulo or autor or edicion or disponibilidad is None:
        return jsonify({"error":"Faltan datos requeidos"}),400
    
    #crear un nuevo libro y guardarlo en la base de datos
    libro=Libro(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad)
    libro.save()
    
    return jsonify(render_libro_detail(libro)),201