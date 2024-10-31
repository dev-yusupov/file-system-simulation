# CLI-Based File System Explorer Documentation

## Overview

This project simulates a basic file system in a command-line interface (CLI) environment. Users can navigate directories, create and delete files and directories, and manage content. The file system is structured using tree data structures, allowing for efficient organization and manipulation of hierarchical data.

## Features

- Create and delete directories
- Create and delete files
- Navigate through directories
- List contents of the current directory
- Move files and directories
- Read and write file content

## Requirements

- Python 3.x
- No external libraries are required

## Running CLI Application

```bash
python file_sys.py
```

## Usage

Upon running the script, you will see a prompt resembling the current directory path, and you can enter commands. Use the following commands to interact with the file system:

### Commands

- `cd <directory>`: Change the current working directory to the specified directory.
Example: `cd Documents`

- `mkdir <directory>`: Create a new directory with the specified name in the current directory.
Example: `mkdir Projects`

- `touch <file>`: Create a new file with the specified name in the current directory.
Example: touch notes.txt

- `rm <file/directory>`: Remove the specified file or directory from the current directory.
Example: rm old_notes.txt

- `ls`: List all files and directories in the current directory.
Example: ls

- `mv <source> <destination>`: Move a file or directory from the source to the destination.
Example: mv notes.txt Archive

- exit: Exit the file system simulation.
Example: exit

### Example Session

```bash
root $ mkdir Documents
root $ cd Documents
Documents $ touch myfile.txt
Documents $ ls
myfile.txt
Documents $ mkdir Projects
Documents $ cd Projects
Projects $ touch project1.py
Projects $ ls
project1.py
Projects $ cd ..
Documents $ ls
myfile.txt  Projects
Documents $ rm myfile.txt
Documents $ ls
Projects
Documents $ exit
```

### Implementation Details

#### Classes

#### 1. Node

- Base class for both `File` and `Directory`.
- **Attributes**:
  - `name`: Name of the file or directory.
  - `parent`: Reference to the parent directory.
  - `created_at`: Timestamp of creation.
  - `updated_at`: Timestamp of last update.

- **Methods**:
  - rename(new_name): Renames the node.
  - get_path(): Returns the full path of the node.

#### 2. File

- Inherits from `Node` and represents a file.
- **Attributes**:
  - `content`: Content of the file.
  - `size`: Size of the file in bytes.

- **Methods**:
  - `write_content(content)`: Writes content to the file.
  - `read_content()`: Reads the content of the file.
  - `delete_content()`: Clears the content of the file.

#### 3. Directory

- Inherits from `Node` and can contain child nodes.
- **Attributes**:
  - `children`: List of child nodes (files and directories).

- **Methods**:
  - `add_child(child)`: Adds a child node.
  - `remove_child(child)`: Removes a child node.
  - `list_contents()`: Lists all child nodes.
  - `find_child(name)`: Finds a child node by name.

#### 4. FileSystem

- Manages the root directory and current working directory.
- **Methods**:
  - `change_directory(dir_name)`: Changes the current directory.
  - `make_directory(dir_name)`: Creates a new directory.
  - `make_file(file_name)`: Creates a new file.
  - `delete_node(name)`: Deletes a file or directory.
  - `move_node(source_name, dest_dir_name)`: Moves a file or directory.
  - `list_contents()`: Lists contents of the current directory.

#### Command Handling

Commands are managed using a command mapping approach. Each command corresponds to a specific function that performs the associated action on the file system.

#### Future Enhancements

- Implement file content manipulation (reading and writing).
- Add file size calculation and display.
- Implement error handling for invalid commands and edge cases.
- Support additional file attributes (e.g., permissions, modification dates).
