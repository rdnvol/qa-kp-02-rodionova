import pytest
from directory import Directory

class TestDirectory:
    mainDirectory = Directory('main')

    def test_directory_init(self):
        name = 'new_name'
        maxElementsNumber = 5
        directory = Directory(name, maxElementsNumber)

        assert directory.name == name

        
    def test_directory_delete(self):
        pass

    def test_list_of_directory_content(self):
        pass

    def test_directory_init(self):
        pass





