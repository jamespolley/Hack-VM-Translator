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
@c0_if_eq
D;JEQ
D=0
@c0_else
0;JMP
(c0_if_eq)
D=-1
(c0_else)
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
@c1_if_eq
D;JEQ
D=0
@c1_else
0;JMP
(c1_if_eq)
D=-1
(c1_else)
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
@c2_if_eq
D;JEQ
D=0
@c2_else
0;JMP
(c2_if_eq)
D=-1
(c2_else)
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
@c3_if_lt
D;JLT
D=0
@c3_else
0;JMP
(c3_if_lt)
D=-1
(c3_else)
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
@c4_if_lt
D;JLT
D=0
@c4_else
0;JMP
(c4_if_lt)
D=-1
(c4_else)
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
@c5_if_lt
D;JLT
D=0
@c5_else
0;JMP
(c5_if_lt)
D=-1
(c5_else)
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
@c6_if_gt
D;JGT
D=0
@c6_else
0;JMP
(c6_if_gt)
D=-1
(c6_else)
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
@c7_if_gt
D;JGT
D=0
@c7_else
0;JMP
(c7_if_gt)
D=-1
(c7_else)
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
@c8_if_gt
D;JGT
D=0
@c8_else
0;JMP
(c8_if_gt)
D=-1
(c8_else)
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


(EXIT)
@EXIT
0;JMP
