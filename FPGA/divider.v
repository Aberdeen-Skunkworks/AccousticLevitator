// fpga4student.com: FPGA projects, VHDL projects, Verilog projects
// Verilog project: Verilog code for clock divider on FPGA
// Top level Verilog code for clock divider on FPGA
module Clock_divider(clock_in, clock_out, divisor, reset);
input clock_in; // input clock on FPGA
output clock_out; // output clock after dividing the input clock by divisor
input reset;
reg[7:0] counter;
input [7:0] divisor;

reg clock_out_driver;
always @(posedge clock_in or negedge reset)
begin
	if (~reset) begin
		counter <= 8'd0;
		clock_out_driver <= 0;
	end else begin
		if(counter==divisor) begin
			counter <= 8'd0;
			clock_out_driver <= ~clock_out_driver;
		end else begin
			counter <= counter + 8'd1;
		end
	end
end
assign clock_out = clock_out_driver;
endmodule