from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from directory import Directory
from binary_file import BinaryFile
from log_text_file import LogTextFile
from buffer_file import BufferFile

app = Flask(__name__)
api = Api(app)

parent = Directory('parent', 20)

binary = BinaryFile("binary_file")
binary.content = "content"

buffer = BufferFile("buffer_file", 10)

directory = Directory("dir1", 2)

log = LogTextFile("log_file")

@app.route('/')

def switch(item, parentPath):
    if item["operation"] == "create":
        switch_create(item, parentPath) 
        return {'message': 'directory is updated'}

    if item["operation"] == "move":
        return switch_move(item, parentPath)


def switch_create(item, parentPath):
    if item["type"] == "dir":
        newDir = Directory(item["name"], item["maxElNumber"], parentPath)
        parentPath.content.append(newDir)

    elif item["type"] == "binaryFile":
        return BinaryFile(item["name"], parentPath)

    elif item["type"] == "bufferFile":
        return BufferFile(item["name"], parentPath)

    elif item["type"] == "logFile":
        return LogTextFile(item["name"], parentPath)

def switch_move(item, parentPath):
    if item["type"] == "dir":
        for child in parentPath.content:
            if child.name == item["name"]:
                if item["path"] == 0:
                    parentPath.__move_content_to_another_dir__(child, parent)
                    child.parent = parent
                else:
                    res = search(parent, item["path"])
                    if res == None:
                        return jsonify({'message': 'directory is not exist'})
                    else:
                        parentPath.__move_content_to_another_dir__(child, res)

    elif item["type"] == "binaryFile":
        for child in parentPath.content:
            if child.name == item["name"]:
                if item["path"] == 0:
                    parentPath.__move_binory_file__(child, parent)
                else:
                    res = search(parent, item["path"])
                    if res == None:
                        return jsonify({'message': 'directory is not exist'})
                    else:
                        child.__move_binory_file__(res)

    # elif item["type"] == "bufferFile":
    #     return Directory(item["name"], item["maxElNumber"], dataParent)

    # elif item["type"] == "logFile":
    #     return Directory(item["name"], item["maxElNumber"], dataParent)


def search(parentDir, searchItem):
    for item in parentDir.content:
        if item.name == searchItem:
            return item
        if type(item) is Directory:
            res = search(item, searchItem) 
            if res != None:
                return res


class DirectoryApi(Resource):
    def __init__(self):
        self.directory = directory

    def get(self):
        data = request.get_json()
        for startDir in parent.content:
            if startDir.name == data["name"]:
                print("=====")
                for i in startDir.content:
                    print(i.name)
                return startDir.__get_content_list__()
            
        return jsonify({'message': 'Directory is not exist'})


    def post(self): 
        data = request.get_json() 
        directory = Directory(data["name"], data["maxElNumber"], parent = parent)
        parent.content.append(directory)
        
        return jsonify({'message': 'Directory is successfully created'})

    def put(self):       
        data = request.get_json()
        
        for startDir in parent.content:
            if startDir.name == data["name"]:

                for element in data["content"]:
                    res = switch(element, startDir)

            return jsonify({'message': 'directory is updated'})
        return jsonify({'message': 'Directory is not exist'})


    def delete(self):
        data = request.get_json()
        dir_for_deleting = data["name"]
        res = search(parent, dir_for_deleting)
        if res == None:
            return jsonify({'message': 'directory is not exist'})
        else:
            p = res.parent
            for i in p.content:
                print(i.name)
            res.__delete_dir__()
            file = search(parent, "binary_file")
            print(file)
            return jsonify({'message': 'directory deleted'})


class BinaryFileApi(Resource):
    def __init__(self):
        self.binary = binary

    def get(self):
        return jsonify({"directory": "true"})

    def post(self): 
        data = request.get_json() 
        
        directory = Directory(data["name"], data["maxElNumber"])
        
        return jsonify({'message': 'Directory is successfully created'})

    def put(self):
        pass    

    def delete(self):
        pass

class BufferApi(Resource):
    def __init__(self):
        self.buffer = buffer

    def get(self):
        return jsonify({"directory": "true"})

    def post(self): 
        data = request.get_json() 
        
        directory = Directory(data["name"], data["maxElNumber"])
        
        return jsonify({'message': 'Directory is successfully created'})

    def put(self):
        pass

    def delete(self):
        pass


class LogTextFileApi(Resource):
    def __init__(self):
        self.logText = LogTextFile

    def get(self):
        return jsonify({"directory": "true"})

    def post(self): 
        data = request.get_json() 
        
        directory = Directory(data["name"], data["maxElNumber"])
        
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