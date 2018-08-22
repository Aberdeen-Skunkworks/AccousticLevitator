`include "dac.v"
module fmq #(parameter OUTPUTS = 88)(input clk, input rst, output [OUTPUTS-1:0] tx, output UART_TX, input UART_RX, output MAIN_CLK_OUT, output RELOAD_OUT, output OE_OUT, input EXT_SYNC, output [4:0] led);
parameter CLOCK=50000000;
parameter FREQ = 40000;
parameter OFFSET_WIDTH = 11;
parameter [OFFSET_WIDTH-2:0] DIVIDE = CLOCK / FREQ / 2 - 1;
parameter DATA_WIDTH = 8;
parameter BAUD = 1250000; //We need to use something that divides nicely into the main clock, especially at high speeds
parameter [15:0] UART_SCALE = CLOCK/(BAUD*8);
parameter VERSION = 8'd7;
reg reload_now;
reg [(OFFSET_WIDTH+1) * OUTPUTS - 1:0] offsets;
wire OE;

//Generate the clocks which drive all of the outputs
genvar j;
generate
	for (j=0; j < OUTPUTS; j=j+1) begin : clock_generator
		clock #(OFFSET_WIDTH) osc(clk, reload_now, offsets[(OFFSET_WIDTH+1)*j+:OFFSET_WIDTH], DIVIDE, offsets[(OFFSET_WIDTH+1)*j+OFFSET_WIDTH], OE, tx[j]);	
	end
endgenerate

//The main clock, outputting the zero-time shift signal, used for sync with other boards and for ensuring reloads happen at the start of a sync cycle.
//This only resets/reloads when the reset line is down (or the external reload is high), unlike the other clocks which go down on reload
assign main_clk_reset = rst && !EXT_SYNC;
clock #(OFFSET_WIDTH) main_clk(clk, main_clk_reset, {OFFSET_WIDTH{1'b0}}, DIVIDE, 1, 1, MAIN_CLK_OUT);

wire dac_clk;
reg [18:0] dac_clk_divisor;
Clock_divider #(19) dac_clk_div(clk, dac_clk, dac_clk_divisor, rst);

reg [8:0] dac_value;
reg [8:0] dac_counter;
reg OE_driver;
always@(posedge dac_clk) begin
	if (!rst) begin
		dac_counter <= 0;
	end else begin
		if (dac_counter < dac_value) begin
			OE_driver <= 1;
		end else begin
			OE_driver <= 0;
		end
		dac_counter <= dac_counter + 1;
	end
end

assign OE = OE_driver;

//dac #(7) output_dac(OE, dac_value, dac_clk, rst);

assign OE_OUT = OE;

reg last_main_clk;
reg reload_next;
//Only reload on a negative transition of the Main Clock, and when a reload is due!
assign falling_main_clk = last_main_clk && !MAIN_CLK_OUT; 
assign main_reload_cond = falling_main_clk && reload_next;
always@(posedge clk) begin
	if (main_reload_cond) begin
		reload_now <= 1'b0; //Reload happens via a low reload line
	end else begin
		reload_now <= 1'b1;
	end
	last_main_clk <= MAIN_CLK_OUT;
end

assign RELOAD_OUT = reload_now;

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
reg [27:0] LEDcounter;
assign led[1] = LEDcounter[24];
assign led[2] = LEDcounter[25];
assign led[3] = LEDcounter[26];
assign led[4] = LEDcounter[27];

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
		offsets <= {OUTPUTS*(OFFSET_WIDTH+1){1'b0}};
		reload_next <= 1'b1; //Trigger a reload next main clock cycle
		cmdbuffer <= 24'd0;
		dac_value		<= 9'd256;
		dac_clk_divisor <= 19'd100;
	end else begin
		if (main_reload_cond) begin
			reload_next <= 1'b0; //Reload is happening, so clear it for the next clock
		end
		
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
            // send byte back out for verification
				cmdbuffer <= {cmdbuffer[0+:16], rx_data};
            tx_data <= rx_data;
            tx_valid <= 1;
         end
      end
		if (cmdbuffer[23]) begin//We have a command
			//Process the command
			case(cmdbuffer[22:21])
			2'b00 : begin
				for (i = 0; i < OUTPUTS; i = i+1)
					if (i == {cmdbuffer[20:16],cmdbuffer[14:13]})
						offsets[(OFFSET_WIDTH+1)*i +: OFFSET_WIDTH+1] <= {cmdbuffer[12:8], cmdbuffer[6:0]};
				//Wipe the command buffer
				cmdbuffer <= 24'd0;
			end
			2'b01 : begin
				//Load divisor
				dac_clk_divisor <= {cmdbuffer[20:16],cmdbuffer[14:8], cmdbuffer[6:0]};
				cmdbuffer <= 24'd0;
			end
			2'b10 : begin //Output the number of outputs configured
				if (!tx_valid) begin
					//We've waited till the previous byte was transmitted, now we can reply 	
					tx_data <= OUTPUTS;
					tx_valid <= 1;
					//Wipe the command buffer
					cmdbuffer <= 24'd0;
				end
			end
			2'b11 : begin //Extra commands
				case(cmdbuffer[20:19])
				2'b00 : begin
					dac_value <= {cmdbuffer[9:8], cmdbuffer[6:0]};
					cmdbuffer <= 24'd0;
				end
				2'b10 : begin
					reload_next <= 1'b1; //Trigger a reload next main clock cycle
					//Wipe the command buffer
					cmdbuffer <= 24'd0;
				end
				2'b01 : begin
					if (!tx_valid) begin
						//We've waited till the previous byte was transmitted, now we can reply 	
						tx_data <= VERSION;
						tx_valid <= 1;
						//Wipe the command buffer
						cmdbuffer <= 24'd0;
					end					
				end
				2'b11 : begin
					// This command byte is for the Arduino and should never get here
				end
				endcase
			end
			default: begin
			   //Command not understood, so ignore it!
				//Wipe the command buffer
				cmdbuffer <= 24'd0;
			end
			endcase
		end
	end
end



endmodule



