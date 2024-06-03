from flask import Blueprint, request, jsonify

from app.models.libro_model import Libro
from app.views.libro_view import render_libro_list, render_libro_detail
from app.utils.decorators import jwt_required, roles_required

# Crear un blueprint para el controlador de libros
libro_bp = Blueprint("libro", __name__)

#Ruta para obtener la lista de libros
@libro_bp.route("/libros", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_libros():
    libros = Libro.get_all()
    return jsonify(render_libro_list(libros))



#ruta para mostrar un libro por id
@libro_bp.route("/libros/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_libro(id):
    libro=Libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error":"Libro no encontrado"}),404

#ruta para crear un nuevo libro

@libro_bp.route("/libros", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
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

#ruta para editar un libro
@libro_bp.route("/libros/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_libro(id):
    libro=Libro.get_by_id(id)
    
    if not libro:
        return jsonify({"error":"Libro no encontrado"}), 404
    data=request.json
    titulo=data.get("titulo")
    autor=data.get("autor")
    edicion=data.get("edicion")
    disponibilidad=data.get("disponibilidad")
    
    libro.update(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad)
    
    return jsonify(render_libro_detail(libro))
    
#ruta para eliminar un libro    
@libro_bp.route("/libros/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_libro(id):
    libro=Libro.get_by_id(id)
    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    libro.delete()
    return "",204
    