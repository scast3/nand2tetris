import os

class VMParser:
    # Constructor
    def __init__(self, filepath):
        self.vm_code = self._load_and_clean_vm_file(filepath)
        self.curr_line = 0
        self.filename = self._extract_filename(filepath)
        self._initialize_command_attributes()

    def has_more_commands(self):
        # Check if there are more commands to process
        return len(self.vm_code) > 0

    def advance(self):
        # Move to the next command and parse it
        self.curr_line += 1
        self._initialize_command_attributes()
        code = self.vm_code.pop(0)
        self.current_command = code
        self._parse_command(code)

    def _initialize_command_attributes(self):
        # Reset command attributes
        self.current_command = None
        self.command_type = None
        self.arg1 = None
        self.arg2 = None

    def _load_and_clean_vm_file(self, filepath):
        # Load the VM file and clean it by removing comments and whitespace
        cleaned_lines = []
        for line in self._read_file(filepath):
            cleaned_line = self._strip_comments_and_whitespace(line)
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
        return cleaned_lines

    def _extract_filename(self, filepath):
        # Extract the filename without the .vm extension
        return os.path.basename(filepath).replace('.vm', '')

    def _read_file(self, filepath):
        # Read the file and return its lines
        with open(filepath, 'r') as file:
            return file.readlines()

    def _strip_comments_and_whitespace(self, line):
        # Remove comments and leading/trailing whitespace from a line
        return line.strip().split("//")[0].strip()

    def _parse_command(self, code):
        # Parse the current command and set its attributes
        if code in ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]:
            self.command_type = "C_ARITHMETIC"
            self.arg1 = code
        elif code.startswith("SP=256"):
            self.command_type = "C_BOOTSTRAP_SP"
            self.arg1 = code
        elif code.startswith("push"):
            self.command_type = "C_PUSH"
            self._set_push_pop_args(code)
        elif code.startswith("pop"):
            self.command_type = "C_POP"
            self._set_push_pop_args(code)
        elif code.startswith("label"):
            self.command_type = "C_LABEL"
            self.arg1 = code.split(" ")[1]
        elif code.startswith("goto"):
            self.command_type = "C_GOTO"
            self.arg1 = code.split(" ")[1]
        elif code.startswith("if-goto"):
            self.command_type = "C_IF"
            self.arg1 = code.split(" ")[1]
        elif code.startswith("function"):
            self.command_type = "C_FUNCTION"
            self._set_function_args(code)
        elif code.startswith("return"):
            self.command_type = "C_RETURN"
        elif code.startswith("call"):
            self.command_type = "C_CALL"
            self._set_function_args(code)
        else:
            raise Exception(f"Unknown command: {code}")

    def _set_push_pop_args(self, code):
        # Parse arguments for push and pop commands
        args = code.split(" ")
        self.arg1 = args[1]
        self.arg2 = int(args[2])

    def _set_function_args(self, code):
        # Parse arguments for function and call commands
        args = code.split(" ")
        self.arg1 = args[1]
        self.arg2 = int(args[2])