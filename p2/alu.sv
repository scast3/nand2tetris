`include "Adder16.sv"
module alu(
    input [15:0] x,
    input [15:0] y,
    input zx,
    input nx,
    input zy,
    input ny,
    input f,
    input no,
    output [15:0] out,
    output zr,
    output ng
);
    // zeroing out the inputs
    assign x1 = (zx == 1) ? x : 16'b0000000000000000;
    assign y1 = (zy == 1) ? y : 16'b0000000000000000;
    
    // selecting negation
    assign x2 = (nx == 1) ? x1 : ~x1;
    assign y2 = (ny == 1) ? y1 : ~y1;

    // selecting function
    assign fresult = (f == 1) ? x2&y2 : x2+y2;

    // negation
    assign out = (no == 1) ? fresult : ~fresult;
    
    assign ng = out[15];

    

endmodule
