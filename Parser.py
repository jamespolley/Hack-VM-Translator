# Handle parsing of input file, break each command into its lexical
# componenets. Ignores whitespace and comments.

import re

class Parser:
    # Command Types
    C_ARITHMETIC  = 1
    C_PUSH        = 2
    C_POP         = 3
    C_LABEL       = 4
    C_GOTO        = 5
    C_IF          = 6
    C_FUNCTION    = 7
    C_RETURN      = 8
    C_CALL        = 9

    # Arithmetic / Logical Commands
    ARITHMETIC = [
        "add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]

    # Arguement 1
    #   to do

    # Arguement 2
    #   to do

    RE_COMMENT = r"//.*\n"
    RE_WHITESPACE = r"\s+"

    def __init__(self, vm_file):
        with open(vm_file, "r") as f:
            self.file = f.readlines()
        self.current_idx = -1
        self.last_idx = len(self.file) - 1
        self.current_line = None
    
    def has_next(self):
        return self.current_idx < self.last_idx
    
    def advance(self):
        self.current_idx += 1
        self.current_line = self.file[self.current_idx]
    
    def get_current_line(self):
        return self.file[self.current_idx]
    
    def parse_current_line(self):
        return Parser._parse_line(self.current_line)
    
    @staticmethod
    def _parse_line(line_to_parse):
        parts = Parser._format_line(line_to_parse)
        if not parts:
            return False
        command_type = Parser._identify_command_type(parts)
        arg_1 = Parser._identify_arg_1(command_type, parts)
        arg_2 = Parser._identify_arg_2(command_type, parts)
        return command_type, arg_1, arg_2
    
    @staticmethod
    def _format_line(line_to_format):
        """Return tuple of formatted line's component parts, filled in with None if part is absent."""
        line = re.sub(Parser.RE_COMMENT, "", line_to_format).strip()
        parts = re.split(Parser.RE_WHITESPACE, line)
        if not parts[0]:
            return False
        while len(parts) < 3:
            parts.append(None)
        return tuple(parts[:3])
    
    @staticmethod
    def _identify_command_type(parts):
        command = parts[0]
        if command == "push": return Parser.C_PUSH
        if command == "pop": return Parser.C_POP
        if command == "label": return Parser.C_LABEL
        if command == "goto": return Parser.C_GOTO
        if command == "if-goto": return Parser.C_IF
        if command == "function": return Parser.C_FUNCTION
        if command == "return": return Parser.C_RETURN
        if command == "call": return Parser.C_CALL
        if command in Parser.ARITHMETIC: return Parser.C_ARITHMETIC
        raise Exception("'{}' does not match any valid command"\
            .format(command))
    
    @staticmethod
    def _identify_arg_1(command_type, parts):
        if command_type == Parser.C_ARITHMETIC: return parts[0]
        if command_type == Parser.C_RETURN: return None
        return parts[1]
    
    @staticmethod
    def _identify_arg_2(command_type, arg_2):
        pass


# tests
p = Parser("assets\MemoryAccess\BasicTest\BasicTest.vm")
print(p.file)
print(p.has_next())
p.advance()

print(p.ARITHMETIC)

print(p._format_line("    asd asdf asdf asdf asdf // asdgasg\n"))
print(p._format_line("    as"))
print(p._parse_line("push asdf 3"))