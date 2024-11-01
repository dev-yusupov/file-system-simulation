from sys import getsizeof
from datetime import datetime
from typing import Optional
from .node import Node

class File(Node):
    def __init__(self, name: str, parent: Optional[Node] = None, created_at: Optional[datetime] = None) -> None:
        super().__init__(name, parent, created_at)
        self.content: str = ""
        self.size: int = 0

    def __repr__(self) -> str:
        return f"File({self.name})"
    
    def write_content(self, content: str) -> None:
        self.content = content
        self.size = getsizeof(self.content)
        self.updated_at = datetime.now()

    def read_content(self) -> str:
        return self.content
    
    def delete_content(self) -> None:
        self.content = ""
        self.size = 0
        self.updated_at = datetime.now()