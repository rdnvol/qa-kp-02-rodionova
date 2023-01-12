from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from directory import Directory
from binary_file import BinaryFile
from log_text_file import LogTextFile
from buffer_file import BufferFile

app = Flask(__name__)
api = Api(app)

parent = Directory('parent', 30)
log = LogTextFile("log_file")
log.parent = parent
parent.content.append(log)

binary = BinaryFile("binary_file")
binary.content = "content"

buffer = BufferFile("buffer_file", 10)

directory = Directory("dir1", 2)

# log = LogTextFile("log_file")

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
            # p = res.parent
            # for i in p.content:
            #     print(i.name)
            res.__delete_dir__()
            # file = search(parent, "binary_file")
            # print(file)
            return jsonify({'message': 'directory deleted'})


class BinaryFileApi(Resource):
    def __init__(self):
        self.binary = binary

    def post(self): 
        data = request.get_json() 
        
        binaryFile = BinaryFile(data["name"], parent = parent)
        binaryFile.content = "It is 'BinaryFile2' file"
        
        return jsonify({'message': 'Binary file is successfully created'})


    def get(self):
        data = request.get_json()
        res = search(parent, data["name"])
        if res == None:
            return jsonify({'message': data["name"] + ' is not exist'})
        else:
            res = res.__read_binory_file__()
            return jsonify({'message': res})

    def put(self):
        data = request.get_json() 

        fileForMove = search(parent, data["name"])
        
        if fileForMove == None:
            return jsonify({'message': data["name"] + ' is not exist'})
        else:
            path = search(parent, data["path"])
            if path == None:
                return jsonify({'message': data["path"] + ' is not exist'})
            else:
                fileForMove.__move_binory_file__(path)
                for i in path.content:
                    print(i.name)
                return jsonify({'message': fileForMove.name + ' was moved to ' + path.name})


    def delete(self):
        data = request.get_json() 

        fileForDelete = search(parent, data["name"])
        if fileForDelete == None:
            return jsonify({'message': data["name"] + ' is not exist'})
        else:
            path = fileForDelete.parent
            fileForDelete.__delete_binory_file__()
            for i in path.content:
                print(i.name)

            print(type(log), log.name, log.parent)
            log.__append_new_line__('message:' + fileForDelete.name + ' removed')
            return jsonify({'message': fileForDelete.name + ' removed'})


class LogTextFileApi(Resource):
    def __init__(self):
        self.logText = LogTextFile

    def post(self): 
        data = request.get_json() 
        
        logFile = LogTextFile(data["name"])
        log.name = logFile.name
        # log.parent = parent
        return jsonify({'message': 'Log file is successfully created'})

    def get(self):
        data = request.get_json() 
        # # print(data["name"])
        # print("==")
        # print("---------------")
        # print(log)
        # print(log.parent.name)
        # for i in parent.content:
        #         print(i)
        # print("---------------")
        # # log.content = "lala"
        # print(log.content)

        res = search(parent, data["name"])
        logContent = res.__read_log_file__()
        print(logContent)

        return jsonify({"log_file_content": logContent})

    def put(self):
        pass

    def delete(self):
        pass


class BufferApi(Resource):
    def __init__(self):
        self.buffer = buffer

    def post(self): 
        data = request.get_json() 
        
        directory = Directory(data["name"], data["maxElNumber"])
        
        return jsonify({'message': 'Directory is successfully created'})

    def get(self):
        data = request.get_json() 
        
        binaryFile = BinaryFile(data["name"], parent = parent)
        binaryFile.content = "It is 'BinaryFile2' file"
        
        return jsonify({'message': 'Binary file is successfully created'})        


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