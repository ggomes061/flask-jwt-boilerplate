from flask import Blueprint, request, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt)

from . import db
from .models import User
from .auth import set_password, verify_password

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exist"}), 400
    
    user = User(username=username, password=set_password(password))
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()

    if user and verify_password(user.password, data.get('password')):
        acess_token = create_access_token(identity={"id": user.id, "role": user.role})
        refresh_token = create_refresh_token(identity={"id": user.id, "role": user.role})
        
        return jsonify(acess_token=acess_token, refresh_token=refresh_token)
    
    return jsonify({"msg": "Bad credentials"}), 401

@api.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@api.route('/admin', methods=['GET'])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get('role') != 'admin':
        return jsonify({"msg": "Admins only!"}, 403)
    
    return jsonify(msg="Welcome admin!"), 200
