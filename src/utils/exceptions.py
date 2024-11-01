class FileSystemError(Exception):
    """
    Base class for file system errors.
    """
    pass


class FileNotFoundError(FileSystemError):
    """
    Raised when a file is not found.
    """
    pass


class DirectoryNotFoundError(FileSystemError):
    """
    Raised when a directory is not found.
    """
    pass


class FileExistsError(FileSystemError):
    """
    Raised when a file already exists.
    """
    pass


class DirectoryExistsError(FileSystemError):
    """
    Raised when a directory already exists.
    """
    pass
