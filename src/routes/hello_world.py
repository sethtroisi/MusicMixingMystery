from flask_restful import Resource
from flask import jsonify

class Welcome(Resource):
    """Hello World"""
    def get(self):
        return jsonify({
                "status": "success",
                "mood": "happy",
        })
