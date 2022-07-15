set filter [list alu_reversed_tb.zero alu_reversed_tb.alu_op alu_reversed_tb.op1 alu_reversed_tb.op2 alu_reversed_tb.result ]
gtkwave::addSignalsFromList $filter
gtkwave::/File/Export/Write_VCD_File_As "/home/edvenson/Icarus-Tests/Tests/alu_reversed/alu_reversed.vcd"
gtkwave::File/Quit