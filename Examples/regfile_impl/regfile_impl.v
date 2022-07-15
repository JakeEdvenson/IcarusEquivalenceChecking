// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2019.2 (lin64) Build 2708876 Wed Nov  6 21:39:14 MST 2019
// Date        : Tue Jun  7 09:58:02 2022
// Host        : CCL15 running 64-bit Ubuntu 20.04.4 LTS
// Command     : write_verilog -force -file /home/edvenson/bfasst/build/xilinx_yosys_impl/bugs/regfile/regfile_impl.v
// Design      : regfile
// Purpose     : This is a Verilog netlist of the current design or from a specific cell of the design. The output is an
//               IEEE 1364-2001 compliant Verilog HDL file that contains netlist information obtained from the input
//               design files.
// Device      : xc7a200tsbg484-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* ECO_CHECKSUM = "1f6948ff" *) 
(* STRUCTURAL_NETLIST = "yes" *)
module regfile_impl
   (clk,
    readData,
    readReg,
    writeData,
    writeReg);
  input clk;
  output readData;
  input readReg;
  input writeData;
  input writeReg;

  wire \<const0> ;
  wire \<const1> ;
  wire GND_2;
  wire clk;
  wire clk_IBUF;
  wire clk_IBUF_BUFG;
  wire readData;
  wire readData0;
  wire readData_OBUF;
  wire readReg;
  wire readReg_IBUF;
  wire writeData;
  wire writeData_IBUF;
  wire writeReg;
  wire writeReg_IBUF;

  GND GND
       (.G(\<const0> ));
  GND GND_1
       (.G(GND_2));
  VCC VCC
       (.P(\<const1> ));
  BUFG clk_IBUF_BUFG_inst
       (.I(clk_IBUF),
        .O(clk_IBUF_BUFG));
  IBUF clk_IBUF_inst
       (.I(clk),
        .O(clk_IBUF));
  OBUF readData_OBUF_inst
       (.I(readData_OBUF),
        .O(readData));
  FDRE #(
    .INIT(1'b0)) 
    readData_reg
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(readData0),
        .Q(readData_OBUF),
        .R(\<const0> ));
  IBUF readReg_IBUF_inst
       (.I(readReg),
        .O(readReg_IBUF));
  (* RTL_RAM_BITS = "2" *) 
  (* RTL_RAM_NAME = "register" *) 
  (* XILINX_LEGACY_PRIM = "RAM16X1D" *) 
  (* ram_addr_begin = "0" *) 
  (* ram_addr_end = "1" *) 
  (* ram_offset = "0" *) 
  (* ram_slice_begin = "0" *) 
  (* ram_slice_end = "0" *) 
  RAM32X1D #(
    .INIT(32'h00000000)) 
    register_reg_0_1_0_0
       (.A0(writeReg_IBUF),
        .A1(\<const0> ),
        .A2(\<const0> ),
        .A3(\<const0> ),
        .A4(GND_2),
        .D(writeData_IBUF),
        .DPO(readData0),
        .DPRA0(readReg_IBUF),
        .DPRA1(\<const0> ),
        .DPRA2(\<const0> ),
        .DPRA3(\<const0> ),
        .DPRA4(GND_2),
        .WCLK(clk_IBUF_BUFG),
        .WE(\<const1> ));
  IBUF writeData_IBUF_inst
       (.I(writeData),
        .O(writeData_IBUF));
  IBUF writeReg_IBUF_inst
       (.I(writeReg),
        .O(writeReg_IBUF));
endmodule
