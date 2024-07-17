from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from src.main.requests.create_user_request import CreateUserRequest

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/user", methods=["POST"])
def create_user():
  try:
    data = CreateUserRequest(**request.json).model_dump()
    return jsonify(data)  
  except ValidationError as error:
    return jsonify(error.errors()), 400

