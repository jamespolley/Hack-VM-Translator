from Parser import Parser
from CodeWriter import CodeWriter


class VMTranslator:
    """
    Main class. Handles the input file. Drives the VM translation process.
    """

    def __init__(self, vm_file_path):
        self.vm_file = self.read(vm_file_path)
        self.file_name = vm_file_path.split("\\")[-1][:-3]
        self.asm_file_path = vm_file_path[:-2]+"asm"
        self.parser = Parser(self.vm_file)
        self.code_writer = CodeWriter(self.file_name)
    
    def translate(self):
        while self.parser.has_next():
            self.parser.advance()
            parsed_line = self.parser.parse_current_line()
            if not parsed_line: continue
            self.code_writer.generate_command(parsed_line)
        self.write(self.asm_file_path, self.code_writer.asm_code)
    
    @staticmethod
    def read(vm_file_path):
        with open(vm_file_path) as f:
            return f.readlines()
    
    @staticmethod
    def write(asm_file_path, asm_code):
        with open(asm_file_path, "w") as f:
            [f.write(line+"\n") for line in asm_code]


        

# tests
vmt = VMTranslator("assets\MemoryAccess\BasicTest\BasicTest.vm")
print(vmt.file_name)
print(vmt.parser.raw_file)
vmt.translate()
# vmt.write()