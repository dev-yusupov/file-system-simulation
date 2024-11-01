import unittest
from datetime import datetime
from src.types.file import File
from src.types.node import Node

class TestFile(unittest.TestCase):
    def test_initialization(self) -> None:
        """
        Test the initialization of the File class
        """
        file: File = File(name='test_file')

        self.assertEqual(file.name, 'test_file')
        self.assertEqual(file.content, '')
        self.assertEqual(file.size, 0)
        self.assertIsInstance(file.created_at, datetime)
        self.assertIsNone(file.parent)

    def test_write_content(self) -> None:
        """
        Test the write_content method of the File class
        """
        file: File = File(name='test_file')
        file.write_content('Hello, World!')
        
        self.assertEqual(file.content, 'Hello, World!')
        self.assertGreater(file.size, 0)
        self.assertIsInstance(file.updated_at, datetime)

    def test_read_content(self) -> None:
        """
        Test the read_content method of the File class
        """
        file: File = File(name='test_file')
        file.write_content('Hello, World!')
        content: str = file.read_content()
        
        self.assertEqual(content, 'Hello, World!')

    def test_delete_content(self) -> None:
        """
        Test the delete_content method of the File class
        """
        file: File = File(name='test_file')
        file.write_content('Hello, World!')
        file.delete_content()
        
        self.assertEqual(file.content, '')
        self.assertEqual(file.size, 0)
        self.assertIsInstance(file.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()