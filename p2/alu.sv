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
    assign x1 = (zx == 1) ? x : 16'b0000000000000000;
    assign notx = ~x

    

endmodule
