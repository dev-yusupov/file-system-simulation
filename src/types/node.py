"""

Node class

This class represents a node in a tree data structure. Each node has
a name, a parent node, and a timestamp for when the node was created.

"""

from typing import Optional, List
from datetime import datetime


class Node:
    """
    A class representing a node in a file system tree
    """

    def __init__(
        self,
        name: str,
        parent: Optional["Node"] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a new Node object

        :param name: The name of the node
        :param parent: The parent node of the node
        :param created_at: The timestamp for when the node was created
        :param updated_at: The timestamp for when the node was last updated

        """
        self.name: str = name
        self.parent: Optional["Node"] = parent
        self.created_at: datetime = (
            created_at if created_at is not None else datetime.now()
        )
        self.updated_at: datetime = (
            updated_at if updated_at is not None else datetime.now()
        )

    def __repr__(self) -> str:
        """
        Return a string representation of the Node object

        :return: A string representation of the Node object
        """

        return f"Node(name={self.name}, parent={self.parent}, created_at={self.created_at}, \
            updated_at={self.updated_at})"

    def rename(self, new_name: str) -> None:
        """
        Rename the node object
        """

        self.name = new_name  # Update the name of the node
        self.updated_at = datetime.now()  # Update the timestamp for when the node was last updated

    def get_path(self) -> str:
        """
        Get the path for the node object
        """
        path: List[str] = []  # Initialize an empty list to store the path

        current_node: Optional["Node"] = self

        while current_node is not None:
            path.insert(0, current_node.name)
            current_node = current_node.parent

        return "/".join(path)
