class CodeWriter(list):
    """Generates symbolic Hack assembly code from parsed VM commands."""

    ARITHMETIC_LOGIC = [
        "add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"
    ] # still needed?
    
    SEGMENTS = {
        "local": "@LCL",        # RAM[1]
        "argument": "@ARG",     # RAM[2]
        "this": "@THIS",        # RAM[3]
        "that": "@THAT"         # RAM[4]
    }
    
    def __init__(self, vm_file):
        self.asm_file = vm_file[:-2] + "asm"
        self.file_name = vm_file.split("\\")[-1][:-3]
        self.comparison_count = 0

    def generate_command(self, parsed_line):
        command, args = parsed_line

        # include comments (new function?)
        comment = "// " + command + " "
        if args[0]:
            comment += args[0] + " "
            if args[1]:
                comment += args[1]
        self.append(comment)

        # Memory Access
        if command in ("push", "pop"):
            self.generate_push_pop(command, args[0], int(args[1]))
        # 
        # Arithmetic / Logic
        elif command in ("add", "sub", "and", "or"):
            self.generate_arithmetic(command)
        elif command in ("neg", "not"):
            self.generate_unary(command)
        elif command in ("lt", "eq", "gt"):
            self.generate_comparison(command)

        # Branching
        elif command == "label":
            # To Do - Week 2
            pass
        # 
        elif command == "goto":
            # To Do - Week 2
            pass
        # 
        elif command == "if-goto":
            # To Do - Week 2
            pass
        # 
        # Function
        elif command == "function":
            # To Do - Week 2
            pass
        # 
        elif command == "call":
            # To Do - Week 2
            pass
        # 
        elif command == "return":
            # To Do - Week 2
            pass
        # 
        else:
            # To Do: raise error, invalid command
            return
        self.append("")
    
    def generate_push_pop(self, command, segment, i):
        # To Do: separate into push/pop functions?? (lot of overlap...)
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
        if_label = "C{}_IF_{}".format(
            self.comparison_count, command.upper())
        else_label = "C{}_ELSE".format(self.comparison_count)
        # 
        # Select values for comparison, find difference
        #   (If difference is negative, then first < second, etc.)
        self.extend(["@SP", "AM=M-1", "D=M", "A=A-1", "D=M-D"])
        # 
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
    
    def write(self):
        with open(self.asm_file, "w") as f:
            for i in self:
                f.write(i)
                f.write("\n")