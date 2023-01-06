class Directory:
    def __init__(self, dirName, content = [], maxElNumber = 0, parent = None) -> None:
        self.name = dirName
        self.content = content
        self.maxElementsNumber = maxElNumber
        self.parent = parent
        pass

    def __delete_dir__(self) -> None:
        del self


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
        content_len = len(self.content)
        self.content = list(filter(lambda x: item in x, self.content))
        if content_len == self.content:
            return item + 'does not exist in the' + self.name

        if type(path) != Directory:
            return 'incorrect path' + path

        if len(path.content) >= path.maxElementsNumber:
            return 'there are no space for new file in directory: ' + path.name

        return path.content.append(item)
        