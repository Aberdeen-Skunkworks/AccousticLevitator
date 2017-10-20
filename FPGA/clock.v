module clock(input clk, input rst, input [23:0] offset, input [23:0] divide, output out);
//50Mhz clock, means 1250 ticks per oscillation, or 650 per transition

//The clock divider
reg[23:0] cnt;
always@(posedge clk or negedge rst)
if(!rst)
	cnt<=offset;
else if(cnt==divide)
	cnt<=24'd0;
else
	cnt<=cnt+1'b1;

//The output driver
reg out_reg;
always@(posedge clk or negedge rst)
if(!rst)
	out_reg<=1'b1;
else if(cnt==divide)
	out_reg<=~out_reg;

assign out=out_reg;
endmodule
