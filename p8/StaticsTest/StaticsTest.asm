
@256
D=A
@SP
M=D

@Sys.init$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Sys.init
0;JMP
(Sys.init$ret.1)

(Class2.set)


@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@Class2.0
M=D

@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@Class2.1
M=D

@0
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@frame
M=D
@5
D=D-A
A=D
D=M
@return_address
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@frame
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@frame
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@frame
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@frame
D=M-D
A=D
D=M
@LCL
M=D
@return_address
A=M
0;JMP

(Class2.get)


@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

@Class2.1
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=D

@LCL
D=M
@frame
M=D
@5
D=D-A
A=D
D=M
@return_address
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@frame
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@frame
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@frame
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@frame
D=M-D
A=D
D=M
@LCL
M=D
@return_address
A=M
0;JMP

(Class1.set)


@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@Class1.0
M=D

@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@Class1.1
M=D

@0
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@frame
M=D
@5
D=D-A
A=D
D=M
@return_address
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@frame
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@frame
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@frame
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@frame
D=M-D
A=D
D=M
@LCL
M=D
@return_address
A=M
0;JMP

(Class1.get)


@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

@Class1.1
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=D

@LCL
D=M
@frame
M=D
@5
D=D-A
A=D
D=M
@return_address
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@frame
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@frame
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@frame
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@frame
D=M-D
A=D
D=M
@LCL
M=D
@return_address
A=M
0;JMP

(Sys.init)


@6
D=A
@SP
A=M
M=D
@SP
M=M+1

@8
D=A
@SP
A=M
M=D
@SP
M=M+1

@Class1.set$ret.4
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Class1.set
0;JMP
(Class1.set$ret.4)

@5
D=A
@0
D=D+A
@addr_5
M=D
@SP
M=M-1
A=M
D=M
@addr_5
A=M
M=D

@23
D=A
@SP
A=M
M=D
@SP
M=M+1

@15
D=A
@SP
A=M
M=D
@SP
M=M+1

@Class2.set$ret.8
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Class2.set
0;JMP
(Class2.set$ret.8)

@5
D=A
@0
D=D+A
@addr_9
M=D
@SP
M=M-1
A=M
D=M
@addr_9
A=M
M=D

@Class1.get$ret.10
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Class1.get
0;JMP
(Class1.get$ret.10)

@Class2.get$ret.11
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Class2.get
0;JMP
(Class2.get$ret.11)

(END)

@END
0;JMP
