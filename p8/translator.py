import sys
import os
from parser import VMParser
from codewriter import CodeWriter


def main():
    input_path = sys.argv[1]
    output_path = determine_output_path(input_path)

    # Remove existing output file if it exists
    if os.path.exists(output_path):
        os.remove(output_path)

    # Handle directory or single file input
    if os.path.isdir(input_path):
        bootstrap(output_path)
        for vm_file in [file for file in os.listdir(input_path) if file.endswith('.vm')]:
            vm_file_path = os.path.join(input_path, vm_file)
            process_vm_file(vm_file_path, output_path)
    elif os.path.isfile(input_path):
        process_vm_file(input_path, output_path)


def determine_output_path(input_path):
    """
    Determine the output file path based on the input path.
    If the input is a directory, the output file will have the same name as the directory.
    If the input is a file, the output file will replace the .vm extension with .asm.
    """
    if os.path.isdir(input_path):
        # Normalize the path to handle trailing slashes
        dir_name = os.path.basename(os.path.normpath(input_path))
        return os.path.join(input_path, dir_name + '.asm')
    elif os.path.isfile(input_path):
        return input_path.replace(".vm", ".asm")


def process_vm_file(vm_file_path, asm_file_path):
    """
    Parse a single VM file and append its translated assembly code to the output ASM file.
    """
    vm_parser = VMParser(vm_file_path)
    asm_writer = CodeWriter(asm_file_path)
    while vm_parser.has_more_commands():
        vm_parser.advance()
        asm_writer.write(vm_parser)
    asm_writer.close()


def bootstrap(asm_file_path):
    """
    Write the bootstrap code to the output ASM file.
    This initializes the stack pointer and calls the Sys.init function.
    """
    asm_writer = CodeWriter(asm_file_path)
    asm_writer.write_boot()
    asm_writer.close()


if __name__ == "__main__":
    main()