class FileSystem:

    def __init__(self):
        self.root = Directory("/")
        self.len_counter = 0
    
    #DO ZMIANY!!!
    def create_directory(self, path):
        self.path = path
        parent = self.root

        FileSystem._validate_path(self.path)

        #tworzenie listy Folderów
        dir_path_list = self.path.split("/")
        dir_path_list.remove("")
        target_directory = dir_path_list[-1]

        #iteracja przez wszystkie Foldery wyciągnięte ze ścieżki i tworzenie obiektu Directory

        for i in range(len(dir_path_list)):
            if dir_path_list[i] in parent.children.keys():
                parent = parent.children[dir_path_list[i]]
                continue

            if dir_path_list[i] not in parent.children.keys():
                if dir_path_list[i] == target_directory:
                    new_directory = Directory(target_directory)
                    parent.add_node(new_directory)
                
                else:
                    raise ValueError(f"Directory '{dir_path_list[i]}' does not exists!")


    def create_file(self, path, contents):
        self.path = path
        self.contents = contents
        parent = self.root

        FileSystem._validate_path(self.path)

        file_path_list = self.path.split("/")
        file_path_list.remove("")
        file_name = file_path_list[-1]

        self.len_counter += len(self.contents)

        new_file = File(file_name)
        new_file.write_contents(self.contents)

        if len(file_path_list) == 1:
            parent.add_node(new_file)

        else:
            for i in range(len(file_path_list)-1):
                try:
                    parent = parent.children[file_path_list[i]]

                except:
                    raise ValueError("Wrong path!")

            parent.add_node(new_file)

    def read_file(self, path):
        self.path = path
        parent = self.root

        file_path_list = self.path.split("/")
        file_path_list.remove("")
        file_name = file_path_list[-1]

        if len(file_path_list) == 1:
            try:
                file_instance = parent.children[file_name]
            except:
                raise ValueError("No such file in this directory!")

        else:
            for i in range(len(file_path_list)-1):
                try:
                    parent = parent.children[file_path_list[i]]
                except:
                    raise ValueError("Wrong path!")
            
            try:
                file_instance = parent.children[file_name]
            except:
                raise ValueError("No such file in this directory!")

        contents = file_instance.contents
        return contents

    def delete_directory_or_file(self, path):
        self.path = path
        parent = self.root

        file_path_list = self.path.split("/")
        file_path_list.remove("")
        file_name = file_path_list[-1]

        if len(file_path_list) == 1:
            try:
                file_instance = parent.children[file_name]
            except:
                raise ValueError("No such file or directory!")
        else:
            for i in range(len(file_path_list)-1):
                try:
                    parent = parent.children[file_path_list[i]]
                except:
                    raise ValueError("Wrong path!")
            
            try:
                file_instance = parent.children[file_name]
            except:
                raise ValueError("No such file or directory!")

        self._recursive_fun(file_instance, parent)

    def size(self):
        return self.len_counter

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")


    def _find_bottom_node(self, node_names):
        pass

        #dodano self
    def _recursive_fun(self, node, parent):
        self.node = node
        self.parent = parent

        if isinstance(node, File):
            self.len_counter -= len(node)
            parent.children.pop(node.name)
            del node
            return
            
        if isinstance(node, Directory):
            if len(node.children) == 0:
                parent.delete_node(node.name)
                return

            else:
                for j in list(node.children.values()):
                    self._recursive_fun(j, node)

        parent.delete_node(node.name)

        

class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)

fs = FileSystem()
fs.create_directory("/dir1")
fs.create_file("/dir1/simon.txt", "ProgrammingExpert is fun!")
fs.size()
fs.delete_directory_or_file("/dir1")
fs.size()