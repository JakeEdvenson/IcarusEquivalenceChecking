`timescale 1ns/1ps

module alu_reversed_tb;

reg [3:0] alu_op = 0;
reg [31:0] op1 = 0;
reg [31:0] op2 = 0;
wire [0:0]  zero;
wire [31:0] result;

initial begin
    $dumpfile("test.vcd");
    $dumpvars(0,alu_reversed_tb);

    # 5 alu_op = 2;
    op1 = 2647136029;
    op2 = 355320445;

    # 5 alu_op = 5;
    op1 = 767721039;
    op2 = 1172194643;

    # 5 alu_op = 13;
    op1 = 1335734964;
    op2 = 2489479236;

    # 5 alu_op = 9;
    op1 = 3870385490;
    op2 = 3063588636;

    # 5 alu_op = 10;
    op1 = 2452360430;
    op2 = 3338293616;

    # 5 alu_op = 10;
    op1 = 1793818797;
    op2 = 1859906646;

    # 5 alu_op = 10;
    op1 = 315292418;
    op2 = 1192999559;

    # 5 alu_op = 1;
    op1 = 1871653752;
    op2 = 1041382995;

    # 5 alu_op = 3;
    op1 = 446833165;
    op2 = 2978051482;

    # 5 alu_op = 0;
    op1 = 2950497471;
    op2 = 1456708403;

    # 5 $finish;
end

/*Regular clock*/
reg clk = 0;
always #1 clk = !clk;

alu_reversed instanceOf (alu_op, op1, op2, result,  zero);

endmodule
