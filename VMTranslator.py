# To Do: improve comments, docstrings?

from Parser import Parser
from CodeWriter import CodeWriter
import sys
import os


class VMTranslator:
    """
    Main class. Handles input, reads the VM file, writes to the assembly file, and drives the VM translation process.
    """

    def __init__(self, input, include_comments=True, include_init_code=True):
        self.file_path = self.get_file_path(input)
        self.input_files = self.process_input(input, self.file_path)
        self.file_path = self.get_file_path(input)
        self.output_file = self.get_output_file(self.file_path)
        self.include_comments = include_comments
        self.include_init_code = include_init_code
    
    def translate(self):
        code_writer = CodeWriter(None,
        include_comments=self.include_comments)
        if self.include_init_code:
            code_writer.generate_init()
        for f in self.input_files:
            vm_code = self.read(f)
            parser = Parser(vm_code)
            code_writer.set_current_file_name(f.split("\\")[-1][:-3])
            while parser.has_next():
                parser.advance()
                parsed_line = parser.parse_current_line()
                if not parsed_line: continue
                code_writer.generate_command(parsed_line)
        code_writer.generate_end()
        output_file_path = os.path.join(
            self.file_path, self.output_file)
        self.write(output_file_path, code_writer)

    @staticmethod
    def process_input(input, file_path):
        input_files = []
        if os.path.isfile(input):
            input_files.append(input)
        else:
            for f in os.listdir(input):
                if f.endswith(".vm"):
                    input_file = os.path.join(file_path, f)
                    input_files.append(input_file)
        return input_files
    
    @staticmethod
    def get_file_path(input):
        if os.path.isdir(input):
            return input
        else:
            return os.path.dirname(input)
    
    @staticmethod
    def get_output_file(file_path):
        return file_path.split("\\")[-1] + ".asm"
    
    @staticmethod
    def read(vm_file_path):
        with open(vm_file_path) as f:
            return f.readlines()
    
    @staticmethod
    def write(asm_file_path, asm_code):
        with open(asm_file_path, "w") as f:
            for line in asm_code:
                f.write(line + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # To do: raise error
        print("ERROR")
    else:
        input_files = sys.argv[1]
        output_file = sys.argv[2]

        vmt = VMTranslator(input_files, output_file)