module newstyle // This is a new style module def
#(parameter real foo = 8, bar=1, baz=2,
parameter signed [7:0] zip = 100)
(
  input x, x2, inout y, y2_long_output,
  output wire [4:1] z, z2
);
endmodule