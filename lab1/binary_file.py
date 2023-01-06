from directory import Directory

class BinaryFile:
    def __init__(self, fileName, parent = None) -> None:
        self.name = fileName
        self.directory = parent
        if type(parent) is Directory:
            parent.content.append(self.name)
        pass

    def __delete_file__(self) -> None:
        del self

    def __move_file__(self, directory, ) -> None:

        pass

    def __read_file__(self) -> None:
        pass