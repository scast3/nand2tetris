module Adder16_tb;
    reg [15:0] A, B;
    reg Cin;
    wire [15:0] Sum;
    wire CarryOut;

    // Instantiate the 16-bit Adder
    Adder16 uut (
        .A(A),
        .B(B),
        .Cin(Cin),
        .Sum(Sum),
        .CarryOut(CarryOut)
    );

    // Test the adder
    initial begin
        // Test Case 1: A = 0x1234, B = 0x5678, Cin = 0
        A = 16'h1234; B = 16'h5678; Cin = 0;
        #10;  // Wait for 10 time units
        $display("A = %h, B = %h, Sum = %h, CarryOut = %b", A, B, Sum, CarryOut);

        // Test Case 2: A = 0xFFFF, B = 0x0001, Cin = 0
        A = 16'hFFFF; B = 16'h0001; Cin = 0;
        #10;
        $display("A = %h, B = %h, Sum = %h, CarryOut = %b", A, B, Sum, CarryOut);

        // Test Case 3: A = 0x8000, B = 0x8000, Cin = 1
        A = 16'h8000; B = 16'h8000; Cin = 1;
        #10;
        $display("A = %h, B = %h, Sum = %h, CarryOut = %b", A, B, Sum, CarryOut);

        // Test Case 4: A = 16'hAAAA, B = 16'h5555, Cin = 0
        A = 16'hAAAA; B = 16'h5555; Cin = 0;
        #10;
        $display("A = %h, B = %h, Sum = %h, CarryOut = %b", A, B, Sum, CarryOut);

        // End the simulation
        $finish;
    end
endmodule
