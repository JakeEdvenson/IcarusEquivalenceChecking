#Input the module name. Stored in var1. var3 and var5 are immediately generated from this.
echo Running Icarus...
echo Input Name of Design - Dont include extensions.
read var1
var2="${var1}_tb"
#echo $var2
var3="${var1}_impl"
var4="${var3}_tb"
var5="${var1}_reversed"
var6="${var5}_tb"

#By default, the file for the original module is generated as a test bench in case further confirmation is needed. 
python /home/edvenson/Icarus-Tests/create_tb.py $var1 $var3 $var5

#Both the goldenfile and reversed-netlist are run through icarus
iverilog -o /home/edvenson/Icarus-Tests/Tests/$var3/dsn /home/edvenson/Icarus-Tests/Tests/$var3/*_tb.v /home/edvenson/Icarus-Tests/Tests/$var3/$var3.v /home/edvenson/Icarus-Tests/Tests/cells_sim.v

vvp /home/edvenson/Icarus-Tests/Tests/$var3/dsn

mv *.vcd /home/edvenson/Icarus-Tests/Tests/$var3/test.vcd

iverilog -o /home/edvenson/Icarus-Tests/Tests/$var5/dsn /home/edvenson/Icarus-Tests/Tests/$var5/*_tb.v /home/edvenson/Icarus-Tests/Tests/$var5/$var5.v /home/edvenson/Icarus-Tests/Tests/cells_sim.v

vvp /home/edvenson/Icarus-Tests/Tests/$var5/dsn

mv *.vcd /home/edvenson/Icarus-Tests/Tests/$var5/test.vcd

#Runs both the goldenfile and the reversed-netlist in waveform. 
gtkwave -o /home/edvenson/Icarus-Tests/Tests/$var3/test.vcd &
gtkwave -o /home/edvenson/Icarus-Tests/Tests/$var5/test.vcd 

#Removes the excess wave files for convenience. Can be disabled if you want to review a file later. 
rm /home/edvenson/Icarus-Tests/Tests/$var1/test.vcd
rm /home/edvenson/Icarus-Tests/Tests/$var1/dsn
rm /home/edvenson/Icarus-Tests/Tests/$var1/test.vcd.fst
rm /home/edvenson/Icarus-Tests/Tests/$var3/test.vcd
rm /home/edvenson/Icarus-Tests/Tests/$var3/dsn
rm /home/edvenson/Icarus-Tests/Tests/$var3/test.vcd.fst
rm /home/edvenson/Icarus-Tests/Tests/$var5/test.vcd
rm /home/edvenson/Icarus-Tests/Tests/$var5/dsn
rm /home/edvenson/Icarus-Tests/Tests/$var5/test.vcd.fst


#This code is in case a user wants to run Vivado to compare against Icarus. Not necessary, but could be useful to have documented.

#echo Test with Vivado as well? 1 for yes, anything else for no.
#read var3
#if [ "$var3" == "1" ] 
#then

#touch test.tcl
#echo create_project temp temp -part xc7a35tcpg236-1 >> test.tcl
#echo add_files -norecurse { /home/edvenson/Icarus-Tests/Tests/$var1/$var1.v /home/edvenson/Icarus-Tests/Tests/$var1/$var2.v } >> test.tcl
#echo set_property top $var2 [get_filesets sim_1] >> test.tcl
#echo launch_simulation >> test.tcl

#export PATH="/tools/Xilinx/Vivado/2019.2/bin:$PATH"

#vivado -nojournal -nolog -source test.tcl

#rm test.tcl

#rm -r temp

#rm -r .Xil

#fi


#This code is if a user wants to generate the original module's waveform.

#iverilog -o /home/edvenson/Icarus-Tests/Tests/$var1/dsn /home/edvenson/Icarus-Tests/Tests/$var1/*_tb.v /home/edvenson/Icarus-Tests/Tests/$var1/$var1.v /home/edvenson/Icarus-Tests/Tests/cells_sim.v

#vvp /home/edvenson/Icarus-Tests/Tests/$var1/dsn

#mv *.vcd /home/edvenson/Icarus-Tests/Tests/$var1/test.vcd

#gtkwave -o /home/edvenson/Icarus-Tests/Tests/$var1/test.vcd &
