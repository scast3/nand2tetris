module mux (A, B, S, C);

    input A, B, S;
    output C;

    assign C = S ? B : A;

endmodule
