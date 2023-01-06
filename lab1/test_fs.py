import pytest
# from io import _io
import io
from directory import Directory
from binary_file import BinaryFile
from log_text_file import LogTextFile
from buffer_file import BufferFile


class TestDirectory: 
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
        print(directory)

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
        file_for_move = BinaryFile('file1')
        file2 = BinaryFile('file2')
        dir_fo_move = Directory('newDir', maxElNumber = 1)

        directory.content.append(file_for_move)
        with pytest.raises(OverflowError):
            directory.__move_content_to_another_dir__(file_for_move, "new_dir")
        
        directory.__move_content_to_another_dir__(file_for_move, dir_fo_move)
        assert len(dir_fo_move.content) == 1
        assert file_for_move.parent == dir_fo_move

        with pytest.raises(OverflowError):
            directory.__move_content_to_another_dir__(file2, dir_fo_move)

        dir_for_move2 = Directory('newDir2', maxElNumber = 1)
        with pytest.raises(OverflowError):
            directory.__move_content_to_another_dir__(file_for_move, dir_for_move2)

        
class TestBinaryFile:
    directory1 = Directory('dir1', 2)
    directory2 = Directory('dir2', 2)
    def test_binary_file_init(self):
        binaryFile = BinaryFile('binary_file1', self.directory1)

        assert len(self.directory1.content) != 0
        
    def test_binary_file_delete(self):
        directory = Directory('dir1')
        binaryFile = BinaryFile('binary_file', directory)

        binaryFile.__delete_binory_file__()
        assert any(item in directory.content for item in directory.content) is False

    def test_move_binary_file(self):
        directory = Directory('dir1')
        binaryFile = BinaryFile('binary_file1', directory)

        binaryFile.__move_binory_file__(self.directory2)
        assert any(binaryFile in self.directory2.content for binaryFile in self.directory2.content) is True


    def test_read_binary_file(self):
        content = 'binary file content'
        binaryFile = BinaryFile('binary_file1')
        binaryFile.content = content

        assert type(binaryFile.__read_binory_file__()) is str


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


