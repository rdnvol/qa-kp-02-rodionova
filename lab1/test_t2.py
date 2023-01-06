import pytest
import types
# from io import _io
import io
from directory import Directory
from binary_file import BinaryFile
from log_text_file import LogTextFile
from buffer_file import BufferFile

class TestBinaryFile:
    def test_binary_file_init(self):
        directory1 = Directory('parent')
        directory2 = Directory('parent')
        print(directory1.content)
        print(directory2.content)
        binaryFile = BinaryFile('binary_file1', directory1)
        # directory.content.append(binaryFile)
        
        print(binaryFile.directory.name)

        assert len(directory1.content) != 0
        
    # def test_binary_file_delete(self):
    #     directory = Directory('parent')
    #     binaryFile = BinaryFile('binary_file', directory)
        
        
    #     directory.__delete_dir__(self)
    #     assert directory != None

    # def test_list_of_directory_content(self):
    #     pass

    # def test_directory_init(self):
    #     pass