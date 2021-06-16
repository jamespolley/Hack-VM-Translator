class CodeWriter(list):
    """Generates symbolic Hack assembly code from parsed VM commands."""

    ARITHMETIC = [
        "add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"
    ]
    
    SEGMENTS = {
        "local": "@LCL",        # RAM[1]
        "argument": "@ARG",     # RAM[2]
        "this": "@THIS",        # RAM[3]
        "that": "@THAT"         # RAM[4]
    }
    
    def __init__(self, vm_file):
        self.asm_file = vm_file[:-2] + "asm"
        self.file_name = vm_file.split("\\")[-1][:-3]

    def generate_command(self, parsed_line):
        command, args = parsed_line

        # include comments
        comment = "// " + command + " "
        if args[0]:
            comment += args[0] + " "
            if args[1]:
                comment += args[1]
        self.append(comment)

        if command in ("push", "pop"):
            self.generate_push_pop(command, args[0], int(args[1]))
        # 
        elif command in self.ARITHMETIC:
            self.generate_arithmetic(command)
        # 
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
                print("got here___error", i)
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
        self.extend(["@SP", "AM=M-1", "D=M", "A=A-1"])
        if command == "add":
            self.append("M=M+D")
        elif command == "sub":
            self.append("M=M-D")
        elif command in ("neg", "eq", "gt", "lt", "and", "or", "not"):
            # To Do: implement
            pass
    
    def write(self):
        with open(self.asm_file, "w") as f:
            for i in self:
                f.write(i)
                f.write("\n")
        
        
# test
cw = CodeWriter("assets\MemoryAccess\BasicTest\BasicTest.vm")
print(cw)
print(cw.file_name)
if 6 not in range(8):
    print("ERROR")