// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


(loop)

@KBD 
D = M

@make_white
D;JEQ           // equal to 0 => white

//Not equal to zero make black
//Write code to make screen black

@8191
D = A 

@i 
M = D       // i= 8191 initialised here


(loopingI)

@i 
D = M
@SCREEN
A = A+D         // A + i done here
M = 0           //Setting M[Screen + i] = 0 
M = !M          // Then negating it will give all 1's 


@i
D = M
M = M-1     //Decrease i
@loopingI
D;JNE       //check i == 0 then break


//*******************************//
@loop
0;JMP
(make_white)
//Write code to make screen white

@8191
D = A 

@j 
M = D       // j= 8191 initialised here


(loopingJ)

@j 
D = M
@SCREEN
A = A+D         // A + j done here
M = 0           //Setting M[Screen + j] = 1


@j
D = M
M = M-1     //Decrease j
@loopingJ
D;JNE       //check j == 0 then break




@loop
0;JMP