import pytest
from directory import Directory
from binary_file import BinaryFile
from log_text_file import LogTextFile
from buffer_file import BufferFile


class TestDirectory:
    mainDirectory = Directory('main')
    main = ""

    def test_directory_init(self):
        name = 'new_name'
        maxElementsNumber = 5
        directory = Directory(name, maxElementsNumber)

        assert directory.name == name

        
    def test_directory_delete(self):
        directory = Directory('main')

        assert directory.__delete_dir__() is None

    def test_list_of_directory_content(self):
        directory = Directory('main')
        
        assert directory.__get_content_list__() == 0

        directory.content = ['file1', Directory('1')]
        assert directory.__get_content_list__() is not None

    def test_directory_move(self):
        directory = Directory('for_move')
        newDir = Directory('newDir', maxElNumber = 5)
        directory.__move_content_to_another_dir__('file1', newDir)
        assert len(newDir.content) != 0



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


