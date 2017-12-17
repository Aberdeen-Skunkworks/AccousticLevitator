module clock#(parameter OFFSET_WIDTH=12)(input clk, input rst, input [OFFSET_WIDTH-1:0] offset, input [OFFSET_WIDTH-3:0] divide, output out);
//50Mhz clock, means 1250 ticks per oscillation, or 625 per transition
//Offset is OFFSET_WIDTH-2 bits of counter, 1 bit of sign, and 1 bit of output enable
//The clock divider
reg[OFFSET_WIDTH-3:0] cnt;
always@(posedge clk or negedge rst)
if (!rst)
	cnt <= offset[OFFSET_WIDTH-3:0];
else if (cnt == divide)
	cnt <= 0;
else
	cnt <= cnt+1'b1;

//The output driver
reg out_reg;
always@(posedge clk or negedge rst)
if(!rst) 
	begin
		if (offset[OFFSET_WIDTH-1])
			out_reg <= offset[OFFSET_WIDTH-2];
		else
			out_reg <= 0;
	end
else if((cnt==divide) && offset[OFFSET_WIDTH-1])
	out_reg <= ~out_reg;

assign out = out_reg;
endmodule
