from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from directory import Directory

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World'

class DirectoryApi(Resource):
    def __init__(self):
        pass

    def get(self):
        return jsonify({"directory": "true"})

    def post(self): 
        data = request.get_json() 
        print('data:', data)
        print('data.name, data.maxElNumber', data["name"], data["maxElNumber"]) 
        directory = Directory(data["name"], data["maxElNumber"])
        print('directory:',directory.name, directory.maxElementsNumber)
        return jsonify({'message': 'Directory is successfully created'})

    def put(self):
        pass

    def delete(self):
        pass

class BinaryFileApi(Resource):
    def __init__(self):
        pass

    def get(self):
        return jsonify({"directory": "true"})

    def post(self): 
        data = request.get_json() 
        print('data:', data)
        print('data.name, data.maxElNumber', data["name"], data["maxElNumber"]) 
        directory = Directory(data["name"], data["maxElNumber"])
        print('directory:',directory.name, directory.maxElementsNumber)
        return jsonify({'message': 'Directory is successfully created'})

    def put(self):
        pass    

    def delete(self):
        pass

class BufferApi(Resource):
    def __init__(self):
        pass

    def get(self):
        return jsonify({"directory": "true"})

    def post(self): 
        data = request.get_json() 
        print('data:', data)
        print('data.name, data.maxElNumber', data["name"], data["maxElNumber"]) 
        directory = Directory(data["name"], data["maxElNumber"])
        print('directory:',directory.name, directory.maxElementsNumber)
        return jsonify({'message': 'Directory is successfully created'})

    def put(self):
        pass

    def delete(self):
        pass


class LogTextFileApi(Resource):
    def __init__(self):
        pass

    def get(self):
        return jsonify({"directory": "true"})

    def post(self): 
        data = request.get_json() 
        print('data:', data)
        print('data.name, data.maxElNumber', data["name"], data["maxElNumber"]) 
        directory = Directory(data["name"], data["maxElNumber"])
        print('directory:',directory.name, directory.maxElementsNumber)
        return jsonify({'message': 'Directory is successfully created'})

    def put(self):
        pass

    def delete(self):
        pass




api.add_resource(DirectoryApi, '/directory')
api.add_resource(BinaryFileApi, '/binaryfile')
api.add_resource(BufferApi, '/bufferfile')
api.add_resource(LogTextFileApi, '/logtextfile')

if __name__ == '__main__':
    app.run(debug=True)