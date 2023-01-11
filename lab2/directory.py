class Directory:
    def __init__(self, dirName, maxElNumber = 0, parent = None):
        self.name = dirName
        self.content = []
        self.maxElementsNumber = maxElNumber
        self.parent = parent


    def __delete_dir__(self) -> None:
        self.parent.content.pop(self.parent.content.index(self))
        for content_item in self.content:
            del content_item
        del self
        return


    def __get_content_list__(self) -> None:
        if len(self.content) == 0:
            return self.name + 'has no files or subdirectories'

        file = '\n'
        for item in self.content:
                file = file + item.name + "\n"

        return file

    def __move_content_to_another_dir__(self, item, path) -> None:
        if type(path) != Directory or None:
            return 'incorrect path' + path

        isitemexist = any(item in self.content for item in self.content)
        if isitemexist:
            if len(path.content) + 1 > path.maxElementsNumber:
                return 'there are no space for new file in directory: ' + path.name

            self.content.pop(self.content.index(item))

            path.content.append(item)
            item.parent = path
            return item.name + " is moved"
        else:
            return item.name + 'does not exist in the ' + self.name


        