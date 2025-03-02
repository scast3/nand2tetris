
module mux_4_way_16(
    input  [15:0] a,
    input  [15:0] b,
    input  [15:0] c,
    input  [15:0] d,
    input  [1:0]  select,
    output [15:0] out
);

    assign out = (select == 2'b00) ? a :
                 (select == 2'b01) ? b :
                 (select == 2'b10) ? c :
                 d;

endmodule