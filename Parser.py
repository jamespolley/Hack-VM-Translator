import re


class Parser:
    """Handles reading of the input file. Formats and parses each line into its lexical components."""

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

    # Regular Expression Patterns for Formatting
    RE_COMMENT = r"//.*\n"
    RE_WHITESPACE = r"\s+"

    def __init__(self, vm_file):
        """Constructor. Open and read the VM code file. Set instance variables to their default values."""
        with open(vm_file, "r") as f:
            self.file = f.readlines()
        self.current_idx = -1
        self.last_idx = len(self.file) - 1
        self.current_line = None
    
    def has_next(self):
        """Return True if there are more lines to parse."""
        return self.current_idx < self.last_idx
    
    def advance(self):
        """Set the current line to the next line in the file."""
        self.current_idx += 1
        self.current_line = self.file[self.current_idx]
    
    def parse_current_line(self):
        """Return a tuple of the current line parsed into identified component parts."""
        return Parser._parse_line(self.current_line)
    
    @staticmethod
    def _parse_line(line_to_parse):
        """Return a tuple of the line parsed into identified component parts."""
        parts = Parser._format_line(line_to_parse)
        if not parts: return False
        command_type = Parser._identify_command_type(parts)
        arg_1 = Parser._identify_arg_1(command_type, parts)
        arg_2 = Parser._identify_arg_2(command_type, parts)
        return command_type, arg_1, arg_2
    
    @staticmethod
    def _format_line(line_to_format):
        """Return a tuple of the line separated into unidentified parts. Fill in tuple with None if any part is absent."""
        line = re.sub(Parser.RE_COMMENT, "", line_to_format).strip()
        parts = re.split(Parser.RE_WHITESPACE, line)
        if not parts[0]: return False
        while len(parts) < 3:
            parts.append(None)
        return tuple(parts[:3])
    
    @staticmethod
    def _identify_command_type(parts):
        """Return an integer constant representing the command type. If command is not found, raise an exception."""
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
        """Return the first arguement. If the command type is C_ARITHMETIC, return the command itself. If the command type is C_RETURN, return None"""
        if command_type == Parser.C_ARITHMETIC: return parts[0]
        if command_type == Parser.C_RETURN: return None
        return parts[1]
    
    @staticmethod
    def _identify_arg_2(command_type, parts):
        """Return the second arguement if the command type is C_PUSH, C_POP, C_FUNCTION, or C_CALL. Otherwise return None."""
        if (command_type == Parser.C_PUSH) or \
            (command_type == Parser.C_POP) or \
            (command_type == Parser.C_FUNCTION) or \
            (command_type == Parser.C_CALL):
            return int(parts[2])
        return None