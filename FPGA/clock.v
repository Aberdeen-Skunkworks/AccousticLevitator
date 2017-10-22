module clock#(parameter OFFSET_WIDTH=11)(input clk, input rst, input [OFFSET_WIDTH-1:0] offset, input [OFFSET_WIDTH-2:0] divide, output out);
//50Mhz clock, means 1250 ticks per oscillation, or 650 per transition
//Offset is OFFSET_WIDTH-1 bits of counter and 1 bit of sign
//The clock divider
reg[OFFSET_WIDTH-2:0] cnt;
always@(posedge clk or negedge rst)
if(!rst)
	cnt<=offset[OFFSET_WIDTH-2:0];
else if(cnt==divide)
	cnt<=0;
else
	cnt<=cnt+1'b1;

//The output driver
reg out_reg;
always@(posedge clk or negedge rst)
if(!rst)
	out_reg<=offset[OFFSET_WIDTH-1];
else if(cnt==divide)
	out_reg<=~out_reg;

assign out=out_reg;
endmodule
