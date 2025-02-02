module dff (
    input D,        
    input CLK,      
    input RST,      
    output reg Q,   
    output Qn       
);

    always @(posedge CLK or posedge RST) begin
        if (RST) begin
            Q <= 1'b0; // reset Q to 0
        end else begin
            Q <= D; //store the D value on rising edge of CLK
        end
    end

    assign Qn = ~Q;

endmodule