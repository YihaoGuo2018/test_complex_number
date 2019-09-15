

from flask import Flask, request
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/test', methods=['get'])
def hello_world():


    return "hello word"





if __name__ == '__main__':
    app.run()