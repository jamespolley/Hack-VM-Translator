# Input:    file.vm
# Output:   file.asm
# 
# Main class. Construct Parser and CodeWriter, go through file, parse
# each line, generate code.

from Parser import Parser

class VMTranslator:
    def __init__(self, vm_file):
        self.parser = Parser(vm_file)
        # to do - add CodeWriter
    
    def translate(self):
        while self.parser.has_next():
            self.parser.advance()
            print(self.parser.parse_current_line())
            
    

# tests
vmt = VMTranslator("assets\MemoryAccess\BasicTest\BasicTest.vm")
vmt.translate()