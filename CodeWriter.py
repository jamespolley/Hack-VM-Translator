# To do:
    # Improve comments (especially for assembly code explanations)
    # Add docstrings??


class CodeWriter(list):
    """
    Generates symbolic Hack assembly code from parsed VM commands.
    """

    ARITHMETIC_LOGIC = [
        "add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"
    ] # still needed?
    
    SEGMENTS = {
        "local": "@LCL",        # RAM[1]
        "argument": "@ARG",     # RAM[2]
        "this": "@THIS",        # RAM[3]
        "that": "@THAT"         # RAM[4]
    }
    
    def __init__(self, file_name):
        self.current_file_name = file_name
        self.current_function = None
        self.comparison_count = 0
        self.call_count = 0

    def generate_command(self, parsed_line):
        command, args = parsed_line

        # Include comments (new function?)
        comment = "// " + command + " "
        if args[0]:
            comment += args[0] + " "
            if args[1]:
                comment += args[1]
        self.append(comment)

        # Memory Access
        if command in ("push", "pop"):
            self.generate_push_pop(command, args[0], int(args[1]))

        # Arithmetic / Logic
        elif command in ("add", "sub", "and", "or"):
            self.generate_arithmetic(command)
        elif command in ("neg", "not"):
            self.generate_unary(command)
        elif command in ("lt", "eq", "gt"):
            self.generate_comparison(command)

        # Branching
        elif command == "label":
            self.generate_label(args[0])
        elif command == "goto":
            self.generate_goto(args[0])
        elif command == "if-goto":
            self.generate_if_goto(args[0])

        # Function
        elif command == "function":
            self.generate_function(args[0], args[1])
        elif command == "call":
            self.generate_function(args[0], args[1])
        elif command == "return":
            self.generate_return()
        
        else:
            # To Do: raise error, invalid command
            return
        self.append("")

    def generate_push_pop(self, command, segment, i):
        # To Do: separate into push/pop functions?? (lot of overlap...)
        # To Do: improve comments
        # 
        # Select target register (for push OR pop)
        if segment == "constant":
            if command == "pop": pass # To Do: raise error
            self.append("@{}".format(i))
        elif segment in ("local", "argument", "this", "that"):
            self.extend([
                self.SEGMENTS[segment], "D=M", "@{}".format(i), "A=D+A"
            ])
        elif segment == "pointer":
            if i not in (0, 1):
                # To Do: raise error, invalid input
                return
            self.append("@R{}".format(3+i))
        elif segment == "temp":
            if i not in range(8):
                # To Do: raise error, invalid input
                return
            self.append("@R{}".format(5+i))
        elif segment == "static":
            self.append("@{}.{}".format(self.file_name, i))
        else:
            # To Do: raise error, segment not valid
            return
        # 
        if command == "push":
            if segment == "constant":
                self.append("D=A")
            else:
                self.append("D=M")
            self.extend([
                '@SP', 'A=M', 'M=D', # *SP = *addr
                '@SP', 'M=M+1' # SP++
            ])
        else: # command == "pop"
            self.extend(['D=A', 
            '@R13', 'M=D', # addr stored in R13
            '@SP', 'AM=M-1', # SP--
            'D=M', # D = *SP
            '@R13', 'A=M', 'M=D' # *addr = D = *SP
        ])

    def generate_arithmetic(self, command):
        # Select values to perform operation
        self.extend(["@SP", "AM=M-1", "D=M", "A=A-1"])
        # 
        # Perform arithmetic operation
        if command == "add":
            self.append("M=M+D")
        elif command == "sub":
            self.append("M=M-D")
        elif command == "and":
            self.append("M=M&D")
        elif command == "or":
            self.append("M=M|D")
        
    def generate_unary(self, command):
        # Select value to perform operation
        self.extend(["@SP", "A=M-1"])
        # 
        # Perform unary operation
        if command == "neg":
            self.append("M=-M")
        elif command == "not":
            self.append("M=!M")
    
    def generate_comparison(self, command):
        # Create labels
        if_label = "c{}_if_{}".format(self.comparison_count, command)
        else_label = "c{}_else".format(self.comparison_count)
        
        # Select values for comparison, find difference
        #   (If difference is negative, then first < second, etc.)
        self.extend(["@SP", "AM=M-1", "D=M", "A=A-1", "D=M-D"])
        
        # Perform comparison operation
        if command == "lt":
            # if first < second, jump to C*_IF_LT
            self.extend(["@"+if_label, "D;JLT"])
        elif command == "eq":
            # if first == second, jump to C*_IF_EQ
            self.extend(["@"+if_label, "D;JEQ"])
        elif command == "gt":
            # if first > second, jump to C*_IF_GT
            self.extend(["@"+if_label, "D;JGT"])
        # 
        # Save boolean result to stack
        self.extend([
            # Set to false (0), jump to C*_ELSE
            "D=0", "@"+else_label, "0;JMP",
            # C*_IF_** jump destination, set to true (-1)
            "({})".format(if_label), "D=-1",
            # C*_ELSE jump destination
            "({})".format(else_label),
            # Save result to stack
            "@SP", "A=M-1", "M=D"
        ])
        # 
        self.comparison_count += 1 # For unique labels

    def generate_label(self, label):
        self.append("({})".format(label))

    def generate_goto(self, label):
        self.extend(["({})".format(label), "0;JMP"])

    def generate_if_goto(self, label):
        # Select top two values on stack, jump if not equal
        self.extend(["@SP", "M=M-1", "A=M", "D=M", "@"+label, "D;JNE"])
        # (can this be simplified??)

    def generate_function(self, function_name, n_vars):
        # Create label
        self.append("({})".format(function_name))

        # Push n_vars local variables onto the stack, initialized at 0
        for i in range(int(n_vars)):
            self.extend(["@SP", "A=M", "M=0", "@SP", "M=M+1"])
        
    def generate_call(self, function_name, n_args):
        # Create function label
        label = "{}$ret.{}".format(function_name, self.call_count)
        # 
        # Push return address (declared below) onto the stack 
        self.extend([
            "{}$ret.{}".format(function_name, self.call_count),
            "D=A", "@SP", "A=M", "M=D", "@SP", "M=M+1"
        ])
        # 
        # Push LCL, ARG, THIS, and THAT pointers onto the stack
        for pointer in ["@LCL", "@ARG", "@THIS", "@THAT"]:
            self.extend([
                pointer, "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"
            ])
        # 
        # Set LCL pointer to SP
        self.extend(["@SP", "D=M", "@LCL", "M=D"])
        # 
        # Set ARG pointer to the start of arguments in the current frame
        self.extend(["@5", "D=D-A", "@"+n_args, "D=D-A", "@ARG", "M=D"])
        # 
        # Goto function
        self.extend(["@"+function_name, "0;JMP"])
        # 
        # Generate return address label
        self.append("({})".format(label))
        # 
        # Increment call count
        self.call_count += 1

    def generate_return(self):
        self.extend([
            # Copy LCL to R13
            "@LCL", "D=M", "@R13", "M=D",

            # Calculate return address, store it in R14
            "D=M", "@5", "A=D-A", "D=M", "@R14", "M=D",

            # Move result to beginning of the ARG segment
            "@SP", "M=M-1", "A=M", "D=M", "@ARG", "A=M", "M=D",

            # Move SP to one after ARG
            "@ARG", "D=M", "@SP", "M=D+1",

            # Restore THAT
            "R13", "AM=M-1", "D=M", "@THAT", "M=D",

            # Restore THIS
            "R13", "AM=M-1", "D=M", "@THIS", "M=D",

             # Restore ARG
            "R13", "AM=M-1", "D=M", "@ARG", "M=D",

             # Restore LCL
            "R13", "AM=M-1", "D=M", "@LCL", "M=D",
            # (above, loop instead?)

            # Jump to return address
            "@R14", "A=M", "0;JMP"
        ])

    def generate_init(self):
        pass

    def generate_end(self):
        pass


