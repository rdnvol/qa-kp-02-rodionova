from directory import Directory

class BufferFile:
    def __init__(self, fileName, maxSize = 0, parent = None) -> None:
        self.name = fileName
        self.parent = parent
        self.content = []
        self.MaxBufferSize = maxSize
        if type(parent) is Directory:
            parent.content.append(self)

    def __delete_buffer_file__(self) -> None:
        self.parent.content.pop(self.parent.content.index(self))
        del self

    def __move_buffer_file__(self, path) -> None:
        if type(path) != Directory or None:
            raise OverflowError('incorrect path' + path)

        if len(path.content) + 1 > path.maxElementsNumber:
            raise OverflowError('there are no space for new file in directory: ' + path.name)

        self.parent.content.pop(self.parent.content.index(self))
        path.content.append(self)
        self.parent = path

    def __push_element__(self, item) -> None:
        if len(self.content) + 1 <=  self.MaxBufferSize:
            self.content.append(item)
        else:
            raise OverflowError('there are no space in buffer file: ' + self.name)

    def __consume_first_line__(self) -> None:
        if len(self.content) >= 1:
            self.content.pop(0)