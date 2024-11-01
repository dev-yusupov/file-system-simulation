from typing import Optional, List
from datetime import datetime
from .node import Node

class Directory(Node):
    children: List[Node]

    def __init__(self, name: str, parent: Optional[Node] = None, created_at: Optional[datetime] = None) -> None: ...
    def __repr__(self) -> str: ...
    def get_path(self) -> str: ...
    def rename(self, new_name: str) -> None: ...
    def add_child(self, child: Node) -> None: ...
    def remove_child(self, child: Node) -> None: ...
    def list_children(self) -> List[Node]: ...