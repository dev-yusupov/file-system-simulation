import unittest
from datetime import datetime
from src.types.node import Node

class TestNode(unittest.TestCase):
    """
    Test cases for the Node class
    """
    def test_name(self) -> None:
        """
        Test the name attribute of the Node class
        """
        root: Node = Node(name='root') # Create a Node object with name 'root'
        self.assertEqual(root.name, 'root')

    def test_update_name(self) -> None:
        """
        Test the rename method of the Node class
        """
        root: Node = Node(name='root') # Create a Node object with name 'root'
        document: Node = Node(name='document', parent=root) # Create a Node object with name 'document' and parent 'root'
        document.rename('file') # Rename the document node to 'file'
        self.assertEqual(document.name, 'file')

    def test_parent(self) -> None:
        """
        Test the parent attribute of the Node class
        """
        home: Node = Node('home') # Create a Node object with name 'home'
        main: Node = Node('main', parent=home) # Create a Node object with name 'main' and parent 'home'
        self.assertEqual(main.parent, home)

    def test_no_parent_no_error(self) -> None:
        """
        Test that the Node class can be instantiated without a parent
        """
        node: Node = Node('root') # No parent specified
        self.assertIsNone(node.parent) # The parent attribute should be None

    def test_created_at(self) -> None:
        """
        Test the created_at attribute of the Node class
        """
        datetime_now: datetime = datetime.now()
        node: Node = Node('root', created_at=datetime_now)
        self.assertIsInstance(node.created_at, datetime)

    def test_get_path(self) -> None:
        """
        Test the get_path method of the Node class
        """
        root: Node = Node(name='root')
        home: Node = Node(name='home', parent=root)
        user: Node = Node(name='user', parent=home)
        self.assertEqual(user.get_path(), 'root/home/user')

if __name__ == '__main__':
    unittest.main()