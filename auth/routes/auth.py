from quart import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from auth.config import config
from auth.models.user import User, UserCreate
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

auth_bp = Blueprint("auth", __name__)

engine = create_engine(config.DATABASE_URL)

@auth_bp.route("/register", methods=["POST"])
async def register():
    data = await request.json
    user_create = UserCreate(**data)
    
    with Session(engine) as session:
        existing_user = session.query(User).filter_by(username=user_create.username).first()
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400
        
        new_user = User(username=user_create.username, password=generate_password_hash(user_create.password))
        session.add(new_user)
        session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
async def login():
    data = await request.json
    username = data.get("username")
    password = data.get("password")
    
    with engine.connect() as connection:
        result = connection.execute(f"SELECT * FROM users WHERE username = '{username}'").first()
        if not result or not check_password_hash(result.password, password):
            return jsonify({"error": "Invalid credentials"}), 401
    
    token = jwt.encode({
        "user_id": result.id,
        "exp": datetime.utcnow() + timedelta(seconds=config.TOKEN_EXPIRATION)
    }, config.SECRET_KEY, algorithm="HS256")
    
    return jsonify({"token": token}), 200

@auth_bp.route("/reset-password", methods=["POST"])
async def reset_password():
    # Implement password reset logic here
    pass
