from typing import Optional, Dict, List
from datetime import datetime
import hashlib

from .node import Node
from src.utils.exceptions import DirectoryExistsError, FileExistsError

class Directory(Node):
    """
    Directory class inherits from Node
    class and represents a directory in the file system.
    """

    def __init__(
        self,
        name: str,
        parent: Optional[Node] = None,
        created_at: Optional[datetime] = None,
    ) -> None:
        super().__init__(name, parent, created_at)

        self.children: Dict[str, "Node"] = {}

    def __repr__(self) -> str:
        return f"Directory(name={self.name}, parent={self.parent}, \
                created_at={self.created_at}, updated_at={self.updated_at})"

    def get_path(self) -> str:
        return super().get_path()

    def rename(self, new_name: str) -> None:
        super().rename(new_name)

    def _hash_name(self, name: str) -> str:
        return hashlib.sha256(name.encode()).hexdigest()

    def add_child(self, child: "Node") -> None:
        """
        Add a child node to the current node
        """

        hashed_name = self._hash_name(child.name)
        
        if hashed_name in self.children:
            if isinstance(child, Directory):
                raise DirectoryExistsError(f"A directory with name {child.name} already exists.")
            
            else:
                raise FileExistsError(f"A file with name {child.name} already exists.")
        
        self.children[hashed_name] = child
        child.parent = self

    def remove_child(self, child: "Node") -> None:
        """
        Remove a child node from the current node
        """
        hashed_name = self._hash_name(child.name)
        if hashed_name not in self.children:
            raise ValueError(f"No child with name {child.name} exists.")
        del self.children[hashed_name]
        child.parent = None

    def list_children(self) -> List["Node"]:
        """
        List the children of the current node
        """
        return list(self.children.values())
