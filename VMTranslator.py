from Parser import Parser
from CodeWriter import CodeWriter


class VMTranslator:
    """Main class. Handles the input file. Drives the VM translation process."""
    def __init__(self, vm_file):
        self.parser = Parser(vm_file)
        self.code_writer = CodeWriter(vm_file)
    
    def translate(self):
        while self.parser.has_next():
            self.parser.advance()
            parsed_line = self.parser.parse_current_line()
            if not parsed_line:
                continue
            self.code_writer.generate_command(parsed_line)
        self.code_writer.write()
        

# tests
vmt = VMTranslator("assets\MemoryAccess\BasicTest\BasicTest.vm")
vmt.translate()
vmt.code_writer.write()