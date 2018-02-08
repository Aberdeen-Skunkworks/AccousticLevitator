module fmq #(parameter OUTPUTS = 88)(input clk, input rst, output [OUTPUTS-1:0] tx, output UART_TX, input UART_RX, output SYNC_CLK_OUT, output [4:0] led);
parameter CLOCK=50000000;
parameter FREQ = 40000;
parameter OFFSET_WIDTH = 12;
parameter [OFFSET_WIDTH-3:0] DIVIDE = CLOCK / FREQ / 2 - 1;
parameter DATA_WIDTH = 8;
parameter BAUD = 460800;
parameter [15:0] UART_SCALE = CLOCK/(BAUD*8);
reg reload_now;
reg [OFFSET_WIDTH * OUTPUTS - 1:0] offsets;

//Generate the clocks which drive all of the outputs
genvar j;
generate
	for (j=0; j < OUTPUTS; j=j+1) begin : clock_generator
		clock #(OFFSET_WIDTH) osc(clk, reload_now, offsets[OFFSET_WIDTH*j+:OFFSET_WIDTH], DIVIDE, tx[j]);	
	end
endgenerate

//The main clock, outputting the zero-time shift signal, used for sync with other boards and for ensuring reloads happen at the start of a sync cycle.
//This only resets/reloads when the reset line is down, unlike the other clocks which go down on reload
clock #(OFFSET_WIDTH) main_clk(clk, rst, {1'b1,{OFFSET_WIDTH-1{1'b0}}}, DIVIDE, SYNC_CLK_OUT);

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
		.prescale(UART_SCALE));

/*First LED just notes the reset events!*/
assign led[0] = ~reload_now;
/*The second LED flashes to indicate the system is working, even under reset*/
reg [32:0] LEDcounter;
assign led[1] = LEDcounter[25];
assign led[2] = LEDcounter[26];
assign led[3] = LEDcounter[27];

//The reset logic for the device
integer i;
reg [23:0] cmdbuffer;
always@(posedge clk or negedge rst)
begin
	if (!rst) begin
		LEDcounter <= 32'd0;
      tx_data <= 0;
      tx_valid <= 0;
      rx_ready <= 0;
		offsets <= {OUTPUTS*OFFSET_WIDTH{1'b0}};
		reload_now <= 1'b0; //Bring the reload line low
		cmdbuffer <= 24'd0;
	end else begin 
		reload_now <= 1'b1; //Bring the reload line high
		LEDcounter <= LEDcounter + 1;
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
				cmdbuffer <= {cmdbuffer[0+:16], rx_data};
         end
      end
		if (cmdbuffer[23]) begin//We have a command
			//Echo the command back
         //tx_data <= cmdbuffer[16+:8];
         //tx_valid <= 1;
			//Process the command
			case(cmdbuffer[22:21])
			2'b00 : begin
				for (i = 0; i < OUTPUTS; i = i+1)
					if (i == {cmdbuffer[20:16],cmdbuffer[14:13]})
						offsets[OFFSET_WIDTH*i +: OFFSET_WIDTH] <= {cmdbuffer[12:8], cmdbuffer[6:0]};
			end
			2'b01 : begin
				reload_now <= 1'b0; //Bring the reload line low
			end
			2'b10 : begin //Output the number of outputs configured
				tx_data <= OUTPUTS;
				tx_valid <= 1;
			end
			default: begin
				tx_data <= 8'd0;
				tx_valid <= 1;
			end
			endcase
			//Wipe the command buffer
			cmdbuffer <= 24'd0;
		end
	end
end



endmodule



