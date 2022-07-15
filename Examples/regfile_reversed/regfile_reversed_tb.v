`timescale 1ns/1ps

module regfile_reversed_tb;

reg [0:0] readReg = 0;
reg [0:0] writeData = 0;
reg [0:0] writeReg = 0;
wire [0:0]  readData;

initial begin
    $dumpfile("test.vcd");
    $dumpvars(0,regfile_reversed_tb);

    # 5 clk = 0;
    readReg = 1;
    writeData = 0;
    writeReg = 0;

    # 5 clk = 0;
    readReg = 1;
    writeData = 0;
    writeReg = 1;

    # 5 clk = 1;
    readReg = 1;
    writeData = 1;
    writeReg = 0;

    # 5 clk = 0;
    readReg = 1;
    writeData = 1;
    writeReg = 1;

    # 5 clk = 0;
    readReg = 1;
    writeData = 1;
    writeReg = 1;

    # 5 clk = 1;
    readReg = 1;
    writeData = 0;
    writeReg = 0;

    # 5 clk = 1;
    readReg = 1;
    writeData = 1;
    writeReg = 1;

    # 5 clk = 0;
    readReg = 0;
    writeData = 1;
    writeReg = 1;

    # 5 clk = 0;
    readReg = 1;
    writeData = 1;
    writeReg = 1;

    # 5 clk = 1;
    readReg = 1;
    writeData = 0;
    writeReg = 1;

    # 5 $finish;
end

/*Regular clock*/
reg clk = 0;
always #1 clk = !clk;

regfile_reversed instanceOf (clk, readReg, writeData, writeReg,  readData);

endmodule
