set filter [list regfile_impl_tb.clk regfile_impl_tb.readData regfile_impl_tb.readReg regfile_impl_tb.writeData regfile_impl_tb.writeReg ]
gtkwave::addSignalsFromList $filter
gtkwave::/File/Export/Write_VCD_File_As "/home/edvenson/Icarus-Tests/Tests/regfile_impl/regfile_impl.vcd"
gtkwave::File/Quit