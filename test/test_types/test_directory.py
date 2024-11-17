import unittest

from src.types import Directory, File
from src.utils.exceptions import DirectoryExistsError, FileExistsError


class TestDirectory(unittest.TestCase):
    def test_directory(self):
        home = Directory("home")
        images = Directory("images", parent=home)

        self.assertEqual(home.name, "home")
        self.assertEqual(home.parent, None)
        self.assertEqual(images.name, "images")
        self.assertEqual(images.parent, home)

    def test_change_directory_name(self):
        home: Directory = Directory("home")
        home.rename("new_home")

        self.assertEqual(home.name, "new_home")

    def test_get_directory_path(self):
        home = Directory("home")
        images = Directory("images", parent=home)

        self.assertEqual(home.get_path(), "home")
        self.assertEqual(images.get_path(), "home/images")

    def test_add_child(self) -> None:
        """
        Test the add_child method of the Node class
        """
        root: Directory = Directory(name="root")
        child: Directory = Directory(name="child")
        root.add_child(child)
        self.assertIn(child, root.children)
        self.assertEqual(child.parent, root)

        # Test adding a file that already exists
        file: File = File(name="file")
        root.add_child(file)

    def test_remove_child(self) -> None:
        """
        Test the remove_child method of the Node class
        """
        root: Directory = Directory(name="root")
        child: Directory = Directory(name="child")
        root.add_child(child)
        root.remove_child(child)
        self.assertNotIn(child, root.children)
        self.assertIsNone(child.parent)

    def test_list_children(self) -> None:
        """
        Test the list_children method of the Node class
        """
        root: Directory = Directory(name="root")
        child1: Directory = Directory(name="child1")
        child2: Directory = Directory(name="child2")
        root.add_child(child1)
        root.add_child(child2)
        self.assertEqual(root.list_children(), [child1, child2])


if __name__ == "__main__":
    unittest.main()
