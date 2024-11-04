from typing import List, Optional

from src.types import Node, Directory, File


class FileSystem:
    def __init__(self):
        self.root = Directory("/root", None)
        self.current = self.root

    def ls(self) -> List[Node]:
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

    def mkdir(self, name) -> Optional[Directory]:
        for child in self.current.children:
            if child.name == name and isinstance(child, Directory):
                print(f"Directory '{name}' already exists.")
                return None

        new_directory = Directory(name=name, parent=self.current)
        self.current.add_child(new_directory)
        print(f"Directory '{name}' created.")

        return new_directory

    def touch(self, name: str) -> Optional[File]:
        for child in self.current.children:
            if child.name == name and isinstance(child, File):
                print(f"File '{name}' already exists.")
                return None
        new_file = File(name=name, parent=self.current)
        self.current.add_child(new_file)
        print(f"File '{name}' created.")
        return new_file

    def cat(self, name: str) -> str:
        """
        Reading the content of a file.
        """
        for child in self.current.children:
            if child.name == name and isinstance(child, File):
                return child.read_content()
        raise FileNotFoundError(f"File '{name}' not found")

    def rm(self, name: str) -> None:
        self.current.remove_child(name)

    def rmdir(self, name) -> None:
        for child in self.current.children:
            if child.name == name and isinstance(child, Directory):
                self.current.remove_child(name)
                return
        raise FileNotFoundError(f"Directory '{name}' not found")

    def find(self, name):
        pass

    def get_current_path(self) -> str:
        return self.current.get_path()

    def __str__(self):
        return str(self.current)
