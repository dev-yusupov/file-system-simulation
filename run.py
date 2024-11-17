from src.root import FileSystem
from src.utils import exceptions

from src.root.config import logger


class FileSystemCLI:
    def __init__(self):
        self.fs = FileSystem()
        self.commands = {
            "mkdir": self.make_directory,
            "touch": self.make_file,
            "cd": self.change_directory,
            "ls": self.list_contents,
            "rm": self.delete_node,
            "mv": self.move_node,
            "help": self.show_help,
            "exit": self.exit_cli,
        }

    def make_directory(self, args):
        if args:
            dir_name = args[0]
            self.fs.mkdir(dir_name)
        else:
            logger.error("Usage: mkdir <directory_name>")

    def make_file(self, args):
        if args:
            file_name = args[0]
            self.fs.touch(file_name)
        else:
            logger.error("Usage: touch <file_name>")

    def change_directory(self, args):
        if args:
            dir_name = args[0]
            self.fs.cd(dir_name)
            logger.info(f"Changed directory to '{dir_name}'.")
        else:
            logger.error("Usage: cd <directory_name>")

    def list_contents(self, args):
        contents = self.fs.ls()
        for node in contents:
            logger.info(node.name)

    def delete_node(self, args):
        if args:
            node_name = args[0]
            try:
                self.fs.rm(node_name)
                logger.info(f"Node '{node_name}' deleted.")
            except FileNotFoundError as e:
                logger.error(e)
        else:
            logger.error("Usage: rm <node_name>")

    def move_node(self, args):
        if len(args) == 2:
            src_name, dest_name = args
            try:
                self.fs.mv(src_name, dest_name)
                logger.info(f"Moved '{src_name}' to '{dest_name}'.")
            except FileNotFoundError as e:
                logger.error(e)
        else:
            logger.error("Usage: mv <source> <destination>")

    def show_help(self, args):
        logger.info("Available commands:")
        for command in self.commands:
            logger.info(command)

    def exit_cli(self, args):
        logger.info("Exiting CLI.")
        exit()

    def run(self):
        logger.info("Welcome to the FileSystem CLI. v1.0.0\n")
        while True:
            current_path = self.fs.get_current_path()
            command_input = input(f"{current_path} $ ").strip().split()
            if not command_input:
                continue
            command = command_input[0]
            args = command_input[1:]
            if command in self.commands:
                self.commands[command](args)
            else:
                try:
                    raise exceptions.UnknownCommandError(
                        f"Unknown command: {command}. Type 'help' for a list of commands."
                    )
                except exceptions.UnknownCommandError as e:
                    logger.error(e)


if __name__ == "__main__":
    FileSystemCLI().run()
