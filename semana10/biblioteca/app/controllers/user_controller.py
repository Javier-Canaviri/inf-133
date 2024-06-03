from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug. security import check_password_hash
from app.models.user_model import User

user_bp=Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data=request.json
    username=data.get("username")
    password=data.get("password")
    roles=data.get("roles")
    
    if not username or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400
    
    new_user=User(username, password,roles)
    new_user.save()
    
    return jsonify({"message": "Usuario creado exitosamente"}), 201

