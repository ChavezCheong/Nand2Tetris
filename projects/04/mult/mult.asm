// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

        @sum    //Init the sum
        M = 0   //Set the sum to 0
        @itr    //Init the iterator
        M = 0 
        @R1
        D = M
        @n
        M = D
    (LOOP)
        @itr
        D = M
        @n
        D = D - M
        @STOP
        D;JEQ   //if i > n goto STOP

        @R0
        D = M
        @sum
        M = M + D
        @itr
        M = M + 1
        @LOOP
        0;JMP
    (STOP)
        @sum
        D = M
        @R2
        M = D
    (END)
        @END
        0;JMP   //Terminates the program