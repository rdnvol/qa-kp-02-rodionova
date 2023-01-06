class Directory:
    def __init__(self, dirName, maxElNumber = 0, parent = None):
        self.name = dirName
        self.content = []
        self.maxElementsNumber = maxElNumber
        self.parent = parent


    def __delete_dir__(self) -> None:
        del self
        return


    def __get_content_list__(self) -> None:
        if len(self.content) == 0:
            return self.name + 'has no files or subdirectories'

        # file = open(self.name + 'list', "w")
        file = self.name + '\n'
        # for item in self.content:
        #     file.write(item + "\n")
        for item in self.content:
            if type(item) == Directory:
                file = file + item.name + "\n"
            else:
                file = file + item + "\n"

        return file

    def __move_content_to_another_dir__(self, item, path) -> None:
        if type(path) != Directory or None:
            raise OverflowError('incorrect path' + path)

        isitemexist = any(item in self.content for item in self.content)
        if isitemexist:
            if len(path.content) + 1 > path.maxElementsNumber:
                raise OverflowError('there are no space for new file in directory: ' + path.name)

            self.content.pop(self.content.index(item))

            path.content.append(item)
            item.parent = path
        else:
            raise OverflowError(item.name + 'does not exist in the ' + self.name)

        return
        