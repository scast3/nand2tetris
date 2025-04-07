import textwrap

class CodeWriter:
    def __init__(self, output_file_path):
        self.output_file = open(output_file_path, "a")

    def write(self, parser):
        asm_code = self.vm_to_asm(parser)
        formatted_asm_code = textwrap.dedent(asm_code)
        self.output_file.write(formatted_asm_code)

    def write_boot(self):
        self.output_file.write(textwrap.dedent(self.bootstrapper()))
        self.output_file.write(textwrap.dedent(self.call_code(1, "Sys.init", 0)))

    def vm_to_asm(self, parser):
        if parser.command_type == "C_ARITHMETIC":
            return self.arith(parser)
        elif parser.command_type == "C_BOOTSTRAP_SP":
            return self.bootstrapper()
        elif parser.command_type == "C_PUSH":
            return self.push_code(parser)
        elif parser.command_type == "C_POP":
            return self.pop_code(parser)
        elif parser.command_type == "C_LABEL":
            return self.label_code(parser)
        elif parser.command_type == "C_GOTO":
            return self.goto_code(parser)
        elif parser.command_type == "C_IF":
            return self.if_code(parser)
        elif parser.command_type == "C_FUNCTION":
            return self.fn_code(parser)
        elif parser.command_type == "C_RETURN":
            return self.return_code(parser)
        elif parser.command_type == "C_CALL":
            return self.call_code(parser.curr_line, parser.arg1, parser.arg2)

    def arith(self, parser):
        if parser.current_command == "add":
            return self.add_code()
        elif parser.current_command == "sub":
            return self.sub_code()
        elif parser.current_command == "neg":
            return self.neg_code()
        
        elif parser.current_command == "and":
            return self.and_code()
        elif parser.current_command == "or":
            return self.or_code()
        elif parser.current_command == "not":
            return self.not_code()
        elif parser.current_command == "eq":
            return self.equals_code(parser)
        elif parser.current_command == "gt":
            return self.greaterthan_code(parser)
        elif parser.current_command == "lt":
            return self.lessthan_code(parser)

    def push_code(self, parser):
        if parser.arg1 == "constant":
            return """
                   @{index}
                   D=A
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1
                   """.format(index=parser.arg2)
        elif parser.arg1 == "local":
            return """
                   @LCL
                   D=M
                   @{index}
                   D=D+A
                   A=D
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1
                   """.format(index=parser.arg2)
        elif parser.arg1 == "argument":
            return """
                   @ARG
                   D=M
                   @{index}
                   D=D+A
                   A=D
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1
                   """.format(index=parser.arg2)
        elif parser.arg1 == "this":
            return """
                   @THIS
                   D=M
                   @{index}
                   D=D+A
                   A=D
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1
                   """.format(index=parser.arg2)
        elif parser.arg1 == "that":
            return """
                   @THAT
                   D=M
                   @{index}
                   D=D+A
                   A=D
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1
                   """.format(index=parser.arg2)
        elif parser.arg1 == "pointer":
            return """
                   @3
                   D=A
                   @{index}
                   D=D+A
                   A=D
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1
                   """.format(index=parser.arg2)
        elif parser.arg1 == "temp":
            return """
                   @5
                   D=A
                   @{index}
                   D=D+A
                   A=D
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1
                   """.format(index=parser.arg2)
        elif parser.arg1 == "static":
            return """
                   @{filename}.{index}
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1
                   """.format(index=parser.arg2, filename=parser.filename)

    def pop_code(self, parser):
        if parser.arg1 == "local":
            return """
                   @LCL
                   D=M
                   @{index}
                   D=D+A
                   @addr_{curr_line}
                   M=D
                   @SP
                   M=M-1
                   A=M
                   D=M
                   @addr_{curr_line}
                   A=M
                   M=D
                   """.format(index=parser.arg2, curr_line=parser.curr_line)
        elif parser.arg1 == "argument":
            return """
                   @ARG
                   D=M
                   @{index}
                   D=D+A
                   @addr_{curr_line}
                   M=D
                   @SP
                   M=M-1
                   A=M
                   D=M
                   @addr_{curr_line}
                   A=M
                   M=D
                   """.format(index=parser.arg2, curr_line=parser.curr_line)
        elif parser.arg1 == "this":
            return """
                   @THIS
                   D=M
                   @{index}
                   D=D+A
                   @addr_{curr_line}
                   M=D
                   @SP
                   M=M-1
                   A=M
                   D=M
                   @addr_{curr_line}
                   A=M
                   M=D
                   """.format(index=parser.arg2, curr_line=parser.curr_line)
        elif parser.arg1 == "that":
            return """
                   @THAT
                   D=M
                   @{index}
                   D=D+A
                   @addr_{curr_line}
                   M=D
                   @SP
                   M=M-1
                   A=M
                   D=M
                   @addr_{curr_line}
                   A=M
                   M=D
                   """.format(index=parser.arg2, curr_line=parser.curr_line)
        elif parser.arg1 == "pointer":
            return """
                   @3
                   D=A
                   @{index}
                   D=D+A
                   @addr_{curr_line}
                   M=D
                   @SP
                   M=M-1
                   A=M
                   D=M
                   @addr_{curr_line}
                   A=M
                   M=D
                   """.format(index=parser.arg2, curr_line=parser.curr_line)
        elif parser.arg1 == "temp":
            return """
                   @5
                   D=A
                   @{index}
                   D=D+A
                   @addr_{curr_line}
                   M=D
                   @SP
                   M=M-1
                   A=M
                   D=M
                   @addr_{curr_line}
                   A=M
                   M=D
                   """.format(index=parser.arg2, curr_line=parser.curr_line)
        elif parser.arg1 == "static":
            return """
                   @SP
                   M=M-1
                   A=M
                   D=M
                   @{filename}.{index}
                   M=D
                   """.format(index=parser.arg2, filename=parser.filename)

    def label_code(self, parser):
        return """
               ({label})
               """.format(label=parser.arg1)

    def goto_code(self, parser):
        return """
               @{label}
               0;JMP
               """.format(label=parser.arg1)

    def if_code(self, parser):
        return """
               @SP
               M=M-1
               A=M
               D=M
               @{label}
               D;JNE
               """.format(label=parser.arg1)

    def fn_code(self, parser):
        push_0 = """
                 @SP
                 A=M
                 M=0
                 @SP
                 M=M+1
                 """ * parser.arg2
        return """
               ({function_name})
               {initialize_local_vars}
               """.format(function_name=parser.arg1, n_vars=parser.arg2, initialize_local_vars=push_0)

    def return_code(self, parser):
        return """
               @LCL
               D=M
               @frame
               M=D
               @5
               D=D-A
               A=D
               D=M
               @return_address
               M=D
               @SP
               M=M-1
               A=M
               D=M
               @ARG
               A=M
               M=D
               @ARG
               D=M+1
               @SP
               M=D
               @frame
               D=M-1
               A=D
               D=M
               @THAT
               M=D
               @2
               D=A
               @frame
               D=M-D
               A=D
               D=M
               @THIS
               M=D
               @3
               D=A
               @frame
               D=M-D
               A=D
               D=M
               @ARG
               M=D
               @4
               D=A
               @frame
               D=M-D
               A=D
               D=M
               @LCL
               M=D
               @return_address
               A=M
               0;JMP
               """
        pass

    def call_code(self, curr_line, function_name, n_args):
        return """
               @{function_name}$ret.{curr_line}
               D=A
               @SP
               A=M
               M=D
               @SP
               M=M+1
               @LCL
               D=M
               @SP
               A=M
               M=D
               @SP
               M=M+1
               @ARG
               D=M
               @SP
               A=M
               M=D
               @SP
               M=M+1
               @THIS
               D=M
               @SP
               A=M
               M=D
               @SP
               M=M+1
               @THAT
               D=M
               @SP
               A=M
               M=D
               @SP
               M=M+1
               @SP
               D=M
               @{n_args}
               D=D-A
               @5
               D=D-A
               @ARG
               M=D
               @SP
               D=M
               @LCL
               M=D

               @{function_name}
               0;JMP
               ({function_name}$ret.{curr_line})
               """.format(curr_line=curr_line, function_name=function_name, n_args=n_args)

    def add_code(self):
        return """
               @SP
               M=M-1
               A=M
               D=M
               A=A-1
               D=D+M
               M=D
               """

    def sub_code(self):
        return """
               @SP
               M=M-1
               A=M
               D=M
               A=A-1
               D=M-D
               M=D
               """

    def neg_code(self):
        return """
               @SP
               A=M-1
               M=-M
               """

    def equals_code(self, parser):
        return """
               @SP
               M=M-1
               A=M
               D=M
               A=A-1
               D=M-D
               @EQ_{curr_line}
               D;JEQ
               @SP
               A=M-1
               M=0
               @END_{curr_line}
               0;JMP
               (EQ_{curr_line})
               @SP
               A=M-1
               M=-1
               (END_{curr_line})
               """.format(curr_line=parser.curr_line)

    def greaterthan_code(self, parser):
        return """
               @SP
               M=M-1
               A=M
               D=M
               A=A-1
               D=M-D
               @GT_{curr_line}
               D;JGT
               @SP
               A=M-1
               M=0
               @END_{curr_line}
               0;JMP
               (GT_{curr_line})
               @SP
               A=M-1
               M=-1
               (END_{curr_line})
               """.format(curr_line=parser.curr_line)

    def lessthan_code(self, parser):
        return """
               @SP
               M=M-1
               A=M
               D=M
               A=A-1
               D=M-D
               @LT_{curr_line}
               D;JLT
               @SP
               A=M-1
               M=0
               @END_{curr_line}
               0;JMP
               (LT_{curr_line})
               @SP
               A=M-1
               M=-1
               (END_{curr_line})
               """.format(curr_line=parser.curr_line)

    def and_code(self):
        return """
               @SP
               M=M-1
               A=M
               D=M
               A=A-1
               M=D&M
               """

    def or_code(self):
        return """
               @SP
               M=M-1
               A=M
               D=M
               A=A-1
               M=D|M
               """

    def not_code(self):
        return """
               @SP
               A=M-1
               M=!M
               """

    def bootstrapper(self):
        return """
               @256
               D=A
               @SP
               M=D
               """

    def close(self):
        self.output_file.close()