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
// Pseudo-code
    
    @SCREEN     // Set pointer to screen
    D = A       
    @screenaddr // screenaddr = 16384
    M = D

    @KBD        // Set pointer to keyboard
    D = A
    @kbdaddr    // kbdaddr = 24576
    M = D

    @8192
    D = A
    @n          // Set n to 8192
    M = D

(CHECKLOOP)     // Start checking loop
    @kbdaddr       
    A = M
    D = M
    @ptr
    M = 0       // Reset the pointer
    @FILLLOOP
    D;JNE       // Check if key is pressed
    @CLEARLOOP
    D;JEQ       // Check if key is not pressed

(FILLLOOP)    
    @ptr
    D = M
    @n
    D = D - M
    @STOP
    D;JEQ
    
    @ptr
    D = M
    @screenaddr
    A = M + D
    M = -1
    @ptr
    M = M + 1
    @FILLLOOP
    0;JMP
(CLEARLOOP)        
    @ptr
    D = M
    @n
    D = D - M
    @STOP
    D;JEQ
    
    @ptr
    D = M
    @screenaddr
    A = M + D
    M = 0
    @ptr
    M = M + 1
    @CLEARLOOP
    0;JMP
(STOP)
    @CHECKLOOP
    0;JMP