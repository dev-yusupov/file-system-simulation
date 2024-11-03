import pytest

from src.types import Directory, File
from src.root import FileSystem

@pytest.fixture
def setup_filesystem():
    fs = FileSystem()
    fs.mkdir(Directory("root"))
    fs.touch(File("root/file1"))

    return fs

def test_create_directory(setup_filesystem):
    fs = setup_filesystem
    fs.touch(File("root/file2"))

    assert fs.ls(Directory("root")) == ["file1", "file2"]