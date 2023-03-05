from flask import Flask, Blueprint
from flask_restful import Api
from src.conversations.conversation_resources import ConversationResources

app = Flask(__name__)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(ConversationResources, '/api/conversations')

app.register_blueprint(api_bp)