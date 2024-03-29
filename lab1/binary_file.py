from directory import Directory

class BinaryFile:
    def __init__(self, fileName, parent = None) -> None:
        self.name = fileName
        self.parent = parent
        self.content = ""
        if type(parent) is Directory:
            parent.content.append(self)

    def __delete_binory_file__(self) -> None:
        self.parent.content.pop(self.parent.content.index(self))
        del self

    def __move_binory_file__(self, path) -> None:
        if type(path) != Directory or None:
            raise OverflowError('incorrect path' + path)

        if len(path.content) + 1 > path.maxElementsNumber:
            raise OverflowError('there are no space for new file in directory: ' + path.name)

        self.parent.content.pop(self.parent.content.index(self))
        path.content.append(self)
        self.parent = path

    def __read_binory_file__(self) -> None:
        return self.content