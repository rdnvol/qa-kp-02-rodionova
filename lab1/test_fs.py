import pytest
import types
# from io import _io
import io
from directory import Directory
from binary_file import BinaryFile
from log_text_file import LogTextFile
from buffer_file import BufferFile


class TestDirectory:
    mainDirectory = Directory('main')
    main = ""

    def test_directory_init(self):
        name = 'first_Directory'
        directory = Directory(name, maxElNumber = 5)

        assert directory.name == name
        assert directory != None
        assert len(directory.content) == 0 
        assert pytest.raises(OverflowError)

        
    def test_directory_delete(self):
        directory = Directory('main')

        assert directory.__delete_dir__() is None

    def test_list_of_directory_content(self):
        directory = Directory('main')
        
        file = directory.__get_content_list__()
        assert type(file) == str

        directory.content = ['file1', Directory('1')]
        
        # assert isinstance(file, io.TextIOWrapper)
        file = directory.__get_content_list__()
        assert type(file) == str
        
    def test_directory_move(self):
        directory = Directory('for_move')
        assert type(directory.__move_content_to_another_dir__('file1', "new_dir")) == str

        directory.content.append('file1')
        assert type(directory.__move_content_to_another_dir__('file1', "new_dir")) == str

        newDir = Directory('newDir', maxElNumber = 1)
        directory.__move_content_to_another_dir__('file1', newDir)
        assert len(newDir.content) == 1

        assert type(directory.__move_content_to_another_dir__('file1', newDir)) == str
        
        assert type(directory.__move_content_to_another_dir__('file2', newDir)) == str



# class TestBinaryFile:
#     binaryFile = BinaryFile('binary_file', 'any content', )

#     def test_binary_file_init(self):
#         name = 'binary_file1'
#         binaryFile = BinaryFile(name)

#         assert binaryFile.name == name

        
#     def test_directory_delete(self):
#         directory = Directory('main')
#         directory.__delete_dir__(self)
#         assert directory != None

#     def test_list_of_directory_content(self):
#         pass

#     def test_directory_init(self):
#         pass


# class TestLogTextFile:
#     mainDirectory = Directory('main')
#     main = ""

#     def test_directory_init(self):
#         name = 'new_name'
#         maxElementsNumber = 5
#         directory = Directory(name, maxElementsNumber)

#         assert directory.name == name

        
#     def test_directory_delete(self):
#         directory = Directory('main')
#         directory.__delete_dir__(self)
#         assert directory != None

#     def test_list_of_directory_content(self):
#         pass

#     def test_directory_init(self):
#         pass


# class TestBufferFile:
    # mainDirectory = Directory('main')
    # main = ""

    # def test_directory_init(self):
    #     name = 'new_name'
    #     maxElementsNumber = 5
    #     directory = Directory(name, maxElementsNumber)

    #     assert directory.name == name

        
    # def test_directory_delete(self):
    #     directory = Directory('main')
    #     directory.__delete_dir__(self)
    #     assert directory != None

    # def test_list_of_directory_content(self):
    #     pass

    # def test_directory_init(self):
    #     pass


