from directory import Directory

class LogTextFile:
    def __init__(self, fileName, parent = None):
        self.name = fileName
        self.parent = parent
        self.content = ""
        if type(parent) is Directory:
            parent.content.append(self)

    def __delete_log_file__(self) -> None:
        self.parent.content.pop(self.parent.content.index(self))
        del self

    def __move_log_file__(self, path):
        print(path)
        if type(path) != Directory or None:
            return'incorrect path: ' + path

        if len(path.content) + 1 > path.maxElementsNumber:
            return 'there are no space for new file in directory: ' + path.name

        self.parent.content.pop(self.parent.content.index(self))
        path.content.append(self)
        self.parent = path
        return  self.name + ' is moved'

    def __read_log_file__(self):
        return self.content

    def __append_new_line__(self, line):
        self.content = self.content + line + '\n'
        return