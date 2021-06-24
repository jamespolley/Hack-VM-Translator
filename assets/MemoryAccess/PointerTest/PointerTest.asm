// push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop pointer 0
@R3
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


// push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop pointer 1
@R4
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


// push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop this 2
@THIS
D=M
@2
A=D+A
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


// push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop that 6
@THAT
D=M
@6
A=D+A
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


// push pointer 0
@R3
D=M
@SP
A=M
M=D
@SP
M=M+1


// push pointer 1
@R4
D=M
@SP
A=M
M=D
@SP
M=M+1


// add 
@SP
AM=M-1
D=M
A=A-1
M=M+D


// push this 2
@THIS
D=M
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1


// sub 
@SP
AM=M-1
D=M
A=A-1
M=M-D


// push that 6
@THAT
D=M
@6
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1


// add 
@SP
AM=M-1
D=M
A=A-1
M=M+D


(EXIT)
@EXIT
0;JMP
