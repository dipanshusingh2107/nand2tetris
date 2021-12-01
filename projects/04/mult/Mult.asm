// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.


@R2         // R2 = sum
M = 0

@R0
D = M 

@i
M = D         // i= r0  hence we will add r1 to r2 r0 times

//Aim : while(i>0)

(Loop)

@i
D = M
@Stop
D;JLE           //if(D<=0) goto stop and D = M[i]


@R1
D = M

@R2
M = M + D       // r2 = r2+r1

@i              //i--
M = M-1

@Loop
0;JMP


(Stop)
@Stop
0;JMP