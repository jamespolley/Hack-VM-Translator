// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@C0_IF_EQ
D;JEQ
D=0
@C0_ELSE
0;JMP
(C0_IF_EQ)
D=-1
(C0_ELSE)
@SP
A=M-1
M=D

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@C1_IF_EQ
D;JEQ
D=0
@C1_ELSE
0;JMP
(C1_IF_EQ)
D=-1
(C1_ELSE)
@SP
A=M-1
M=D

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@C2_IF_EQ
D;JEQ
D=0
@C2_ELSE
0;JMP
(C2_IF_EQ)
D=-1
(C2_ELSE)
@SP
A=M-1
M=D

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@C3_IF_LT
D;JLT
D=0
@C3_ELSE
0;JMP
(C3_IF_LT)
D=-1
(C3_ELSE)
@SP
A=M-1
M=D

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@C4_IF_LT
D;JLT
D=0
@C4_ELSE
0;JMP
(C4_IF_LT)
D=-1
(C4_ELSE)
@SP
A=M-1
M=D

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@C5_IF_LT
D;JLT
D=0
@C5_ELSE
0;JMP
(C5_IF_LT)
D=-1
(C5_ELSE)
@SP
A=M-1
M=D

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@C6_IF_GT
D;JGT
D=0
@C6_ELSE
0;JMP
(C6_IF_GT)
D=-1
(C6_ELSE)
@SP
A=M-1
M=D

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@C7_IF_GT
D;JGT
D=0
@C7_ELSE
0;JMP
(C7_IF_GT)
D=-1
(C7_ELSE)
@SP
A=M-1
M=D

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@C8_IF_GT
D;JGT
D=0
@C8_ELSE
0;JMP
(C8_IF_GT)
D=-1
(C8_ELSE)
@SP
A=M-1
M=D

// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 53
@53
D=A
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

// push constant 112
@112
D=A
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

// neg 
@SP
A=M-1
M=-M

// and 
@SP
AM=M-1
D=M
A=A-1
M=M&D

// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or 
@SP
AM=M-1
D=M
A=A-1
M=M|D

// not 
@SP
A=M-1
M=!M

