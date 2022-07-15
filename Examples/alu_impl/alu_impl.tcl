set filter [list alu_impl_tb.zero alu_impl_tb.alu_op alu_impl_tb.op1 alu_impl_tb.op2 alu_impl_tb.result ]
gtkwave::addSignalsFromList $filter
gtkwave::/File/Export/Write_VCD_File_As "/home/edvenson/Icarus-Tests/Tests/alu_impl/alu_impl.vcd"
gtkwave::File/Quit
