import unittest
from src.types.directory import Directory
from src.types.file import File


class TestIntegration(unittest.TestCase):


    def test_file_operations(self) -> None:
        """
        Test file operations within a directory
        """
        root: Directory = Directory(name="root")
        home: Directory = Directory(name="home", parent=root)
        file1: File = File(name="file1", parent=home)

        root.add_child(home)
        home.add_child(file1)

        file1.write_content("Hello, World!")
        self.assertEqual(file1.read_content(), "Hello, World!")
        self.assertGreater(file1.size, 0)

        file1.delete_content()
        self.assertEqual(file1.read_content(), "")
        self.assertEqual(file1.size, 0)

    def test_directory_operations(self) -> None:
        """
        Test directory operations
        """
        root: Directory = Directory(name="root")
        home: Directory = Directory(name="home", parent=root)
        documents: Directory = Directory(name="documents", parent=home)
        file1: File = File(name="file1", parent=documents)

        root.add_child(home)
        home.add_child(documents)
        documents.add_child(file1)

        self.assertEqual(root.get_path(), "root")
        self.assertEqual(home.get_path(), "root/home")
        self.assertEqual(documents.get_path(), "root/home/documents")
        self.assertEqual(file1.get_path(), "root/home/documents/file1")

        home.rename("new_home")
        self.assertEqual(documents.get_path(), "root/new_home/documents")
        self.assertEqual(file1.get_path(), "root/new_home/documents/file1")

    def test_remove_node(self) -> None:
        """
        Test removing nodes from a directory
        """
        root: Directory = Directory(name="root")
        home: Directory = Directory(name="home", parent=root)
        file1: File = File(name="file1", parent=home)

        root.add_child(home)
        home.add_child(file1)

        home.remove_child(file1)
        self.assertNotIn(file1, home.list_children())
        self.assertIsNone(file1.parent)


if __name__ == "__main__":
    unittest.main()
