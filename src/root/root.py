from src.types import Directory, File

class FileSystem:
    def __init__(self):
        self.root = Directory("/root", None)
        self.current = self.root

    def ls(self):
        return self.current.list_children()

    def cd(self, directory_name):
        if directory_name == "..":
            if self.current.parent is not None:
                self.current = self.current.parent
        else:
            for child in self.current.children:
                if child.name == directory_name and isinstance(child, Directory):
                    self.current = child
                    return
            raise FileNotFoundError(f"Directory '{directory_name}' not found")

    def mkdir(self, name):
        new_directory = Directory(name=name, parent=self.current)
        self.current.add_child(new_directory)

    def touch(self, name):
        new_file = File(name=name, parent=self.current)
        self.current.add_child(new_file)

    def cat(self, name):
        for child in self.current.children:
            if child.name == name and isinstance(child, File):
                return child.read()
        raise FileNotFoundError(f"File '{name}' not found")

    def rm(self, name):
        self.current.remove_child(name)

    def rmdir(self, name):
        for child in self.current.children:
            if child.name == name and isinstance(child, Directory):
                self.current.remove_child(name)
                return
        raise FileNotFoundError(f"Directory '{name}' not found")

    def find(self, name):
        return self.current.find(name)

    def __str__(self):
        return str(self.current)