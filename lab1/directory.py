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
        return len(self.content)

    def __move_content_to_another_dir__(self, item, path) -> None:
        self.content = list(filter(lambda x: item in x, self.content))
        return path.content.append(item)