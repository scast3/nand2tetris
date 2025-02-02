module tb_mux_4_way_16;

    // Declare testbench signals
    reg [15:0] a, b, c, d;
    reg [1:0] select;
    wire [15:0] out;

    // Instantiate the mux_4_way_16 module
    mux_4_way_16 uut (
        .a(a),
        .b(b),
        .c(c),
        .d(d),
        .select(select),
        .out(out)
    );

    // Initialize signals and apply test vectors
    initial begin
        // Monitor the output
        $monitor("Time: %0t | select: %b | a: %h | b: %h | c: %h | d: %h | out: %h", 
                  $time, select, a, b, c, d, out);
        
        // Test case 1: select = 00
        a = 16'hAAAA; b = 16'hBBBB; c = 16'hCCCC; d = 16'hDDDD;
        select = 2'b00; #10;

        // Test case 2: select = 01
        select = 2'b01; #10;

        // Test case 3: select = 10
        select = 2'b10; #10;

        // Test case 4: select = 11
        select = 2'b11; #10;

        // Finish the simulation
        $finish;
    end

endmodule
