from fs_api import app
import json
from directory import Directory
from binary_file import BinaryFile
from log_text_file import LogTextFile
from buffer_file import BufferFile

class TestDirectoryApi():
    
    def test_create_directory(self):
        response = app.test_client().post('/directory', json={
            "name": "directory1",
            "maxElNumber": 4,
        })
        assert response.data != None

    def test_put_directory_(self):
        response = app.test_client().put('/directory', json={
            "name": "directory1",
            "content": [
                {
                    "operation": "create",
                    "type":"dir", 
                    "name":"child", 
                    "maxElNumber": 1
                }, 
                {
                    "operation": "create",
                    "type":"dir", 
                    "name":"childForDel", 
                    "maxElNumber": 2
                }, 
                {
                    "operation": "create",
                    "type":"binaryFile", 
                    "name":"binary_file", 
                }
            ]
        })
        
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': 'directory is updated'}

        response = app.test_client().put('/directory', json={
            "name": "directory1",
            "content": [
                {
                    "operation": "move",
                    "type": "dir",
                    "name":"child", 
                    "path": "childForDel"
                }
                # {
                #     "operation": "move",
                #     "type": "binaryFile",
                #     "name":"binary_file", 
                #     "path": "childForDel"
                # }
            ]
        })

        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': 'directory is updated'}


    def test_get_directory_list(self):
        response = app.test_client().get('/directory', json={
            "name": "directory1"
        })

        res = json.loads(response.data.decode('utf-8'))
        assert res == '\nchildForDel\nbinary_file\n'

    def test_delete_directory_(self):
        response = app.test_client().delete('/directory', json={
            "name": "test"
        })
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': 'directory is not exist'}

        response = app.test_client().delete('/directory', json={
            "name": "childForDel"
        })
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': 'directory deleted'}

class TestBinaryFileApi():
    
    def test_create_binary_file(self):
        response = app.test_client().post('/binaryfile', json={
            "name": "binary_file2",
            "parent": "parent"
        })
        assert response.data != None

    def test_get_binaryFile(self):
        response = app.test_client().get('/binaryfile', json={
            "name": "binary_file2",
        })
        
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': "It is 'BinaryFile2' file"}

        response = app.test_client().get('/binaryfile', json={
            "name": "binary_file",
        })
        
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': ""}

        response = app.test_client().get('/binaryfile', json={
            "name": "binary",
        })
        
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': 'binary is not exist'}

 
    def test_put_binaryFile(self):
        response = app.test_client().put('/binaryfile', json={
            "name": "binary_file2",
            "path": "directory1"
        })

        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'binary_file2 was moved to directory1'}

        response = app.test_client().put('/binaryfile', json={
            "name": "binary",
            "path": "directory1"
        })

        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'binary is not exist'}

        response = app.test_client().put('/binaryfile', json={
            "name": "binary_file2",
            "path": "dirdirdir"
        })

        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'dirdirdir is not exist'}

    def test_delete_binary_file_(self):
        response = app.test_client().delete('/binaryfile', json={
            "name": "binary_file"
        })
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'binary_file removed'}

        response = app.test_client().delete('/binaryfile', json={
            "name": "binary_file"
        })
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'binary_file is not exist'}


class TestLogFileApi():
    
    def test_create_log_file(self):
        response = app.test_client().post('/logtextfile', json={
            "name": "log_file_1",
            "path": "parent"
        })

        assert response.data != None

    def test_get_log_file(self):
        response = app.test_client().get('/logtextfile', json={
            "name": "log_file",
        })
        
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'log_file_content': 'message:binary_file removed\n'}

        response = app.test_client().get('/logtextfile', json={
            "name": "log_file_1",
        })
        
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'log_file_content': ''}

    def test_patch_log_file_path(self):
        response = app.test_client().patch('/logtextfile', json={
            "name": "log_file_1",
            "path": "directory1"
        })
        
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': 'log_file_1 is moved'}


    def test_delete_directory_(self):
        response = app.test_client().delete('/logtextfile', json={
            "name": "log_file_1"
        })
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'log_file_1 deleted'}

        response = app.test_client().delete('/logtextfile', json={
            "name": "log_file_1"
        })
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'log_file_1 is not exist'}


class TestBufferFileApi():
    
    def test_create_buffer_file(self):
        response = app.test_client().post('/bufferfile', json={
            "name": "buffer_file",
            "maxSize": 4,
            "parent": "directory1"
        })
        assert response.data != None

 
    def test_patch_buffer_file(self):
        response = app.test_client().patch('/bufferfile', json={
            "name": "buffer_file",
            "operation": "push",
            "line": "line1"
        })

        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': 'the line was pushed'}

        response = app.test_client().patch('/bufferfile', json={
            "name": "buffer_file",
            "operation": "push",
            "line": "line2"
        })

        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message': 'the line was pushed'}

        response = app.test_client().patch('/bufferfile', json={
            "name": "buffer_file",
            "operation": "consume"
        })

        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'first line was consume'}

        response = app.test_client().patch('/bufferfile', json={
            "name": "buffer_file",
            "operation": "move",
            "path": "parent"
        })

        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'buffer_file is moved'}


    def test_delete_buffer_file_(self):
        response = app.test_client().delete('/bufferfile', json={
            "name": "buffer_file"
        })
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'buffer_file deleted'}

        response = app.test_client().delete('/bufferfile', json={
            "name": "buffer_file"
        })
        res = json.loads(response.data.decode('utf-8'))
        assert res == {'message':'buffer_file is not exist'}