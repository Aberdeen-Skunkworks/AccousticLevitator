module fmq #(parameter OUTPUTS = 16)(input clk, input rst, output [OUTPUTS-1:0] tx, output UART_TX, input UART_RX);
parameter CLOCK=50000000;
parameter FREQ = 40000;
parameter DIVIDE=CLOCK/FREQ/2-1;
parameter DATA_WIDTH=8;
parameter BAUD=115200;
parameter CLOCK_WIDTH = 10;
reg reload;
reg [CLOCK_WIDTH*OUTPUTS-1:0] offsets;

//Generate the parallel clocks
genvar j;
generate
	for (j=0; j < OUTPUTS; j=j+1) begin : clock_generator
		clock #(CLOCK_WIDTH) osc(clk, reload, offsets[CLOCK_WIDTH*j+:CLOCK_WIDTH], DIVIDE, tx[j]);	
	end
endgenerate

reg [DATA_WIDTH-1:0]  tx_data;
reg                   tx_valid;
wire tx_ready;
wire [DATA_WIDTH-1:0]  rx_data;
wire                   rx_valid;
reg rx_ready;

wire uart_rst;
assign uart_rst = ~rst; 

uart #(DATA_WIDTH) 
	uart_inst (.clk(clk), .rst(uart_rst), 
		.input_axis_tdata(tx_data), .input_axis_tvalid(tx_valid), .input_axis_tready(tx_ready),
		.output_axis_tdata(rx_data), .output_axis_tvalid(rx_valid), .output_axis_tready(rx_ready), 
		.rxd(UART_RX), .txd(UART_TX), .tx_busy(), .rx_busy(), .rx_overrun_error(), .rx_frame_error(), 
		.prescale(CLOCK/(BAUD*8)));

//The reset logic for the device
integer i;
reg [23:0] cmdbuffer;
always@(posedge clk or negedge rst)
begin
	if (!rst) begin
      tx_data <= 0;
      tx_valid <= 0;
      rx_ready <= 0;
		for (i=0; i < OUTPUTS; i=i+1) begin
			offsets[CLOCK_WIDTH*i+:CLOCK_WIDTH] = (i * 10);
		end
		reload <= 1'b0; //Bring the reload line low
		cmdbuffer <= 24'd0;
	end else begin 
		reload <= 1'b1; //Bring the reload line high
      if (tx_valid) begin
			// attempting to transmit a byte
         // so can't receive one at the moment
         rx_ready <= 0;
         // if it has been received, then clear the valid flag
         if (tx_ready) begin
				tx_valid <= 0;
         end
      end else begin
			// ready to receive byte
         rx_ready <= 1;
         if (rx_valid) begin
				// got one, so make sure it gets the correct ready signal
            // (either clear it if it was set or set it if we just got a
            // byte out of waiting for the transmitter to send one)
            rx_ready <= ~rx_ready;
            // send byte back out
            //tx_data <= rx_data;
            //tx_valid <= 1;
				cmdbuffer[16+:8] <= cmdbuffer[8+:8];
				cmdbuffer[8+:8] <= cmdbuffer[0+:8];
				cmdbuffer[0+:8] <= rx_data;
         end
      end
		if (cmdbuffer[23]) begin//We have a command
			//Echo the command back
         tx_data <= cmdbuffer[16+:8];
         tx_valid <= 1;
			//Process the command
			
			//Wipe the command buffer
			cmdbuffer <= 24'd0;
		end
	end
end

endmodule


