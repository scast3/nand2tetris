import sys
import os


class VMTranslator:
    def __init__(self):
        self.gt_count = 0
        self.lt_count = 0
        self.eq_count = 0
        self.file_name = ""
        self.pop_d = "@SP\nAM=M-1\nD=M\n"
        self.get_m = "@SP\nA=M-1\n"
        self.diff_true = "D=M-D\nM=-1\n"
        self.make_false = "@SP\nA=M-1\nM=0\n"
        self.push = "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        self.math_ops = {
            "sub": "-",
            "add": "+",
            "and": "&",
            "or": "|",
            "neg": "-",
            "not": "!",
        }
        self.seg_pointers = {
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT",
            "local": "LCL",
            "temp": "5",
            "pointer": "3",
        }
        self.translations = {
            "add": self.math_2_arg,
            "sub": self.math_2_arg,
            "or": self.math_2_arg,
            "and": self.math_2_arg,
            "neg": self.math_1_arg,
            "not": self.math_1_arg,
            "eq": self.math_bool,
            "gt": self.math_bool,
            "lt": self.math_bool,
            "push": self.push_fun,
            "pop": self.pop_fun,
        }

    def math_2_arg(self, command):
        math_op = self.math_ops.get(command[0], command[0] + " not found")
        assign = f"M=M{math_op}D\n"
        return self.pop_d + self.get_m + assign

    def math_1_arg(self, command):
        math_op = self.math_ops.get(command[0], command[0] + " not found")
        assign = f"M={math_op}M\n"
        return self.get_m + assign

    def math_bool(self, command):
        if command[0] == "gt":
            name = f"gtTrue{self.gt_count}"
            test = f"@{name}\nD;JGT\n"
            self.gt_count += 1
        elif command[0] == "eq":
            name = f"eqTrue{self.eq_count}"
            test = f"@{name}\nD;JEQ\n"
            self.eq_count += 1
        elif command[0] == "lt":
            name = f"ltTrue{self.lt_count}"
            test = f"@{name}\nD;JLT\n"
            self.lt_count += 1
        else:
            return f"// Invalid boolean operation: {command[0]}\n"

        label = f"({name})\n"
        return self.pop_d + self.get_m + self.diff_true + test + self.make_false + label

    def push_fun(self, command):
        segment, index = command[1], command[2]
        if segment == "constant":
            value = f"@{index}\nD=A\n"
        elif segment == "static":
            value = f"@{self.file_name}.{index}\nD=M\n"
        else:
            tp_a = "A" if segment in ["temp", "pointer"] else "M"
            pointer = self.seg_pointers.get(segment, f"invalid segment: {segment}\n")
            index_d = f"@{index}\nD=A\n"
            value_d = f"@{pointer}\nA={tp_a}+D\nD=M\n"
            value = index_d + value_d

        return value + self.push

    def pop_fun(self, command):
        segment, index = command[1], command[2]
        if segment == "static":
            pointer = f"@{self.file_name}.{index}\n"
            return self.pop_d + pointer + "M=D\n"

        tp_a = "A" if segment in ["temp", "pointer"] else "M"
        pointer = self.seg_pointers.get(segment, f"invalid segment: {segment}\n")
        index_d = f"@{index}\nD=A\n"
        address_r13 = f"@{pointer}\nD={tp_a}+D\n@R13\nM=D\n"
        change = "@R13\nA=M\nM=D\n"

        return index_d + address_r13 + self.pop_d + change

    def initialize(self, file):
        file.write(f"\n/// Initializing {file.name} ///\n\n")

    def translate(self, line):
        command = line.split("/")[0].strip().split()
        if not command:
            return ""
        func = self.translations.get(
            command[0], lambda x: f"\n// Whoops! {command[0]} not found\n\n"
        )
        return func(command)

    def process_files(self, path, infiles, outfile):
        for f in infiles:
            self.file_name = f[:-3]
            outfile.write(f"\n// Translating {f} //\n\n")
            with open(os.path.join(path, f)) as infile:
                for line in infile:
                    outfile.write(self.translate(line))

    def main(self):
        if len(sys.argv) < 2:
            print("Usage: python3 translator.py <file.vm | directory>")
            sys.exit(1)

        arg = sys.argv[1]
        infiles = []

        if os.path.isfile(arg):
            path = os.path.dirname(arg)
            base = os.path.basename(arg)[:-3]
            infiles.append(base + ".vm")
        elif os.path.isdir(arg):
            path = arg
            base = os.path.basename(arg)
            infiles = [file for file in os.listdir(arg) if file.endswith(".vm")]
        else:
            print("Invalid input path")
            sys.exit(1)

        outfile_path = os.path.join(path, base + ".asm")
        with open(outfile_path, "w") as outfile:
            self.initialize(outfile)
            self.process_files(path, infiles, outfile)


if __name__ == "__main__":
    translator = VMTranslator()
    translator.main()