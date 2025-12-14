from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///fallback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret')

db = SQLAlchemy(app)

# (mantenha todos os seus modelos aqui — Supermercado, Produto, etc.)

# JWT e rotas (igual ao anterior, mas com SECRET_KEY dinâmico)
SECRET_KEY = app.config['SECRET_KEY']

# ... (mantenha as funções token_required, /login, /pedido, etc.)