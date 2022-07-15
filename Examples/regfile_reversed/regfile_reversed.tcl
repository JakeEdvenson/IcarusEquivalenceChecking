set filter [list regfile_reversed_tb.clk regfile_reversed_tb.readData regfile_reversed_tb.readReg regfile_reversed_tb.writeData regfile_reversed_tb.writeReg ]
gtkwave::addSignalsFromList $filter
gtkwave::/File/Export/Write_VCD_File_As "/home/edvenson/Icarus-Tests/Tests/regfile_reversed/regfile_reversed.vcd"
gtkwave::File/Quit