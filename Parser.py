import re


class Parser:
    """
    Handles traversal and parsing of each line into its lexical components.
    """
    
    # Regular Expression Patterns for Formatting
    RE_COMMENT = r"//.*\n"
    RE_WHITESPACE = r"\s+"

    def __init__(self, vm_file):
        """Constructor. Open and read the VM code file. Set instance variables to their default values."""
        self.raw_file = vm_file
        self.current_idx = -1
        self.last_idx = len(self.raw_file) - 1
        self.current_line = None
    
    def has_next(self):
        """Return True if there are more lines to parse."""
        return self.current_idx < self.last_idx
    
    def advance(self):
        """Set the current line to the next line in the file."""
        self.current_idx += 1
        self.current_line = self.raw_file[self.current_idx]
    
    def parse_current_line(self):
        """Return a tuple containing: (1) command, (2) inner tuple containing arguments. If stripped line is empty, return False. If no arguments, append None as default."""
        line = re.sub(Parser.RE_COMMENT, "", self.current_line).strip()
        tokens = re.split(Parser.RE_WHITESPACE, line)
        if not tokens[0]:
            return False
        while len(tokens) < 2:
            tokens.append(None)
        if len(tokens) > 3:
            # TO DO: raise error, too many arguments
            return False
        command, args = tokens[0], tuple(tokens[1:])
        return command, args