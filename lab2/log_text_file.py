from directory import Directory

class LogTextFile:
    def __init__(self, fileName, parent = None):
        self.name = fileName
        self.parent = parent
        self.content = ""
        if type(parent) is Directory:
            parent.content.append(self)

    def __delete_log_file__(self):
        self.parent.content.pop(self.parent.content.index(self))
        del self

    def __move_log_file__(self, path):
        if type(path) != Directory or None:
            raise OverflowError('incorrect path' + path)

        if len(path.content) + 1 > path.maxElementsNumber:
            raise OverflowError('there are no space for new file in directory: ' + path.name)

        self.parent.content.pop(self.parent.content.index(self))
        path.content.append(self)
        self.parent = path

    def __read_log_file__(self):
        return self.content

    def __append_new_line__(self, line):
        self.content = self.content + line + '\n'
        return