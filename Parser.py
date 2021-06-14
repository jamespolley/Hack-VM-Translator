# Handle parsing of input file, break each command into its lexical
# componenets. Ignores whitespace and comments.

class Parser:
    # Command Types
    NOT_A_COMMAND = 0
    C_ARITHMETIC = 1
    C_PUSH = 2
    C_POP = 3
    C_LABEL = 4
    C_GOTO = 5
    C_IF = 6
    C_FUNCTION = 7
    C_RETURN = 8
    C_CALL = 9

    # Arguement 1
    #   to do

    # Arguement 2
    #   to do

    def __init__(self, vm_file):
        with open(vm_file, "r") as f:
            self.file = f.readlines()
        self.current_idx = -1
        self.last_idx = len(self.file) - 1
        self.current_line = None
    
    def has_next(self):
        return self.current_idx <= self.last_idx
    
    def advance(self):
        self.current_idx += 1
    
    def get_current(self):
        return self.file[self.current_idx]
    
    def parse(self):
        command_type = 123 # temp
        arg_1 = 456 # temp
        arg_2 = 789 # temp
        return command_type, arg_1, arg_2
    
    def get_command_type(self):
        pass

    def get_arg_1(self):
        pass

    def get_arg_2(self):
        pass


# tests
p = Parser("assets\MemoryAccess\BasicTest\BasicTest.vm")
print(p.file)
print(p.parse())
print(p.has_next())
p.advance()
print(p.get_current())