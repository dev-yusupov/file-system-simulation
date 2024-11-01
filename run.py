from src.root import FileSystem


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
            print(f"Directory '{dir_name}' created.")
        else:
            print("Usage: mkdir <directory_name>")

    def make_file(self, args):
        if args:
            file_name = args[0]
            self.fs.touch(file_name)
            print(f"File '{file_name}' created.")
        else:
            print("Usage: touch <file_name>")

    def change_directory(self, args):
        if args:
            dir_name = args[0]
            self.fs.cd(dir_name)
            print(f"Changed directory to '{dir_name}'.")
        else:
            print("Usage: cd <directory_name>")

    def list_contents(self, args):
        contents = self.fs.ls()
        for node in contents:
            print(node.name)

    def delete_node(self, args):
        if args:
            node_name = args[0]
            try:
                self.fs.rm(node_name)
                print(f"Node '{node_name}' deleted.")
            except FileNotFoundError as e:
                print(e)
        else:
            print("Usage: rm <node_name>")

    def move_node(self, args):
        if len(args) == 2:
            src_name, dest_name = args
            try:
                self.fs.mv(src_name, dest_name)
                print(f"Moved '{src_name}' to '{dest_name}'.")
            except FileNotFoundError as e:
                print(e)
        else:
            print("Usage: mv <source> <destination>")

    def show_help(self, args):
        print("Available commands:")
        for command in self.commands:
            print(command)

    def exit_cli(self, args):
        print("Exiting CLI.")
        exit()

    def run(self):
        print("Welcome to the FileSystem CLI. v1.0.0\n")
        while True:
            command_input = input("fs> ").strip().split()
            if not command_input:
                continue
            command = command_input[0]
            args = command_input[1:]
            if command in self.commands:
                self.commands[command](args)
            else:
                print(
                    f"Unknown command: {command}. Type 'help' for a list of commands."
                )


if __name__ == "__main__":
    FileSystemCLI().run()
