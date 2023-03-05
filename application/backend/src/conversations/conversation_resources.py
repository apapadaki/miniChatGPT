# Conversation related Rest resources
from flask_restful import Resource


class ConversationResources(Resource):
    def get(self):
        return {"hi": "hi"}
