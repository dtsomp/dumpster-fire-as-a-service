from flask import Flask, request
from flask_restful import Resource, Api
import random, os

app = Flask(__name__)

api = Api(app)

dumpsterfires = [
    { 
        'desc': 'container',
        'url': 'https://media.giphy.com/media/26FPy3QZQqGtDcrja/giphy.gif'
    },
    { 
        'desc': 'under control',
        'url': 'https://media.giphy.com/media/ZNBXrNJfS3bQk/giphy.gif'
    },
    {
        'desc': 'selfie',
        'url': 'https://media.giphy.com/media/SyqAptNmn3fyM/giphy-downsized-large.gif'
    },
    {
        'desc': 'floating',
        'url': 'https://media.giphy.com/media/QLyhWVTvAHbAbAdWcp/giphy.gif'
    }
]

class Random(Resource):
    def get(self):
        if len(dumpsterfires) > 0:    
            return random.choice(dumpsterfires)
        return { 'dumpster fire': None }, 404

        

api.add_resource(Random, '/random')
port = int(os.environ.get('PORT', 33507))
app.run(port=port)
