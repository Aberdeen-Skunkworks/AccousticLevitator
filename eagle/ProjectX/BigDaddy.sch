<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="8.4.3">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="2" name="Route2" color="1" fill="3" visible="no" active="no"/>
<layer number="3" name="Route3" color="4" fill="3" visible="no" active="no"/>
<layer number="4" name="Route4" color="1" fill="4" visible="no" active="no"/>
<layer number="5" name="Route5" color="4" fill="4" visible="no" active="no"/>
<layer number="6" name="Route6" color="1" fill="8" visible="no" active="no"/>
<layer number="7" name="Route7" color="4" fill="8" visible="no" active="no"/>
<layer number="8" name="Route8" color="1" fill="2" visible="no" active="no"/>
<layer number="9" name="Route9" color="4" fill="2" visible="no" active="no"/>
<layer number="10" name="Route10" color="1" fill="7" visible="no" active="no"/>
<layer number="11" name="Route11" color="4" fill="7" visible="no" active="no"/>
<layer number="12" name="Route12" color="1" fill="5" visible="no" active="no"/>
<layer number="13" name="Route13" color="4" fill="5" visible="no" active="no"/>
<layer number="14" name="Route14" color="1" fill="6" visible="no" active="no"/>
<layer number="15" name="Route15" color="4" fill="6" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="24" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="Parts">
<packages>
<package name="CORE3S500E">
<description>&lt;b&gt;Core3S500E&lt;/b&gt;&lt;p&gt;
The Xilinx Spartan 3E FPGA board from WaveShare.</description>
<pad name="P$161" x="5" y="27" drill="0.9" diameter="1.27"/>
<text x="-21.62" y="28.54" size="1.27" layer="25">&gt;NAME</text>
<text x="-15.27" y="28.54" size="1.27" layer="27">&gt;VALUE</text>
<pad name="P$163" x="3" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$165" x="1" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$168" x="-1" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$172" x="-3" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$178" x="-5" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$180" x="-7" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$185" x="-9" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$187" x="-11" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$190" x="-13" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$193" x="-15" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$197" x="-17" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$200" x="-19" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$203" x="-21" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$2" x="-23" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$4" x="-25" y="27" drill="0.9" diameter="1.27"/>
<pad name="P$162" x="5" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$164" x="3" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$167" x="1" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$171" x="-1" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$177" x="-3" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$179" x="-5" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$181" x="-7" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$186" x="-9" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$189" x="-11" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$192" x="-13" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$196" x="-15" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$199" x="-17" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$202" x="-19" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$205" x="-21" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$3" x="-23" y="25" drill="0.9" diameter="1.27"/>
<pad name="P$5" x="-25" y="25" drill="0.9" diameter="1.27"/>
<pad name="GND@2" x="-25" y="19" drill="0.9" diameter="1.27"/>
<pad name="P$8" x="-25" y="17" drill="0.9" diameter="1.27"/>
<pad name="P$11" x="-25" y="15" drill="0.9" diameter="1.27"/>
<pad name="P$15" x="-25" y="13" drill="0.9" diameter="1.27"/>
<pad name="P$18" x="-25" y="11" drill="0.9" diameter="1.27"/>
<pad name="P$22" x="-25" y="9" drill="0.9" diameter="1.27"/>
<pad name="P$24" x="-25" y="7" drill="0.9" diameter="1.27"/>
<pad name="P$28" x="-25" y="5" drill="0.9" diameter="1.27"/>
<pad name="P$30" x="-25" y="3" drill="0.9" diameter="1.27"/>
<pad name="P$33" x="-25" y="1" drill="0.9" diameter="1.27"/>
<pad name="P$35" x="-25" y="-1" drill="0.9" diameter="1.27"/>
<pad name="GND@4" x="-25" y="-3" drill="0.9" diameter="1.27"/>
<pad name="P$39" x="-25" y="-5" drill="0.9" diameter="1.27"/>
<pad name="P$41" x="-25" y="-7" drill="0.9" diameter="1.27"/>
<pad name="P$45" x="-25" y="-9" drill="0.9" diameter="1.27"/>
<pad name="P$48" x="-25" y="-11" drill="0.9" diameter="1.27"/>
<pad name="P$50" x="-25" y="-13" drill="0.9" diameter="1.27"/>
<pad name="P$60" x="-25" y="-15" drill="0.9" diameter="1.27"/>
<pad name="P$62" x="-25" y="-17" drill="0.9" diameter="1.27"/>
<pad name="P$64" x="-25" y="-19" drill="0.9" diameter="1.27"/>
<pad name="P$69" x="-25" y="-21" drill="0.9" diameter="1.27"/>
<pad name="P$75" x="-25" y="-23" drill="0.9" diameter="1.27"/>
<pad name="P$77" x="-25" y="-25" drill="0.9" diameter="1.27"/>
<pad name="3,3V@2" x="-23" y="19" drill="0.9" diameter="1.27"/>
<pad name="P$9" x="-23" y="17" drill="0.9" diameter="1.27"/>
<pad name="P$12" x="-23" y="15" drill="0.9" diameter="1.27"/>
<pad name="P$16" x="-23" y="13" drill="0.9" diameter="1.27"/>
<pad name="P$19" x="-23" y="11" drill="0.9" diameter="1.27"/>
<pad name="P$23" x="-23" y="9" drill="0.9" diameter="1.27"/>
<pad name="P$25" x="-23" y="7" drill="0.9" diameter="1.27"/>
<pad name="P$29" x="-23" y="5" drill="0.9" diameter="1.27"/>
<pad name="P$31" x="-23" y="3" drill="0.9" diameter="1.27"/>
<pad name="P$34" x="-23" y="1" drill="0.9" diameter="1.27"/>
<pad name="P$36" x="-23" y="-1" drill="0.9" diameter="1.27"/>
<pad name="5V@2" x="-23" y="-3" drill="0.9" diameter="1.27"/>
<pad name="P$40" x="-23" y="-5" drill="0.9" diameter="1.27"/>
<pad name="P$42" x="-23" y="-7" drill="0.9" diameter="1.27"/>
<pad name="P$47" x="-23" y="-9" drill="0.9" diameter="1.27"/>
<pad name="P$49" x="-23" y="-11" drill="0.9" diameter="1.27"/>
<pad name="P$55" x="-23" y="-13" drill="0.9" diameter="1.27"/>
<pad name="P$61" x="-23" y="-15" drill="0.9" diameter="1.27"/>
<pad name="P$63" x="-23" y="-17" drill="0.9" diameter="1.27"/>
<pad name="P$65" x="-23" y="-19" drill="0.9" diameter="1.27"/>
<pad name="P$74" x="-23" y="-21" drill="0.9" diameter="1.27"/>
<pad name="P$76" x="-23" y="-23" drill="0.9" diameter="1.27"/>
<pad name="P$82" x="-23" y="-25" drill="0.9" diameter="1.27"/>
<pad name="3,3V@1" x="23" y="19" drill="0.9" diameter="1.27"/>
<pad name="P$153" x="23" y="17" drill="0.9" diameter="1.27"/>
<pad name="P$151" x="23" y="15" drill="0.9" diameter="1.27"/>
<pad name="P$147" x="23" y="13" drill="0.9" diameter="1.27"/>
<pad name="P$145" x="23" y="11" drill="0.9" diameter="1.27"/>
<pad name="P$140" x="23" y="9" drill="0.9" diameter="1.27"/>
<pad name="P$138" x="23" y="7" drill="0.9" diameter="1.27"/>
<pad name="P$135" x="23" y="5" drill="0.9" diameter="1.27"/>
<pad name="P$133" x="23" y="3" drill="0.9" diameter="1.27"/>
<pad name="P$129" x="23" y="1" drill="0.9" diameter="1.27"/>
<pad name="P$127" x="23" y="-1" drill="0.9" diameter="1.27"/>
<pad name="5V@1" x="23" y="-3" drill="0.9" diameter="1.27"/>
<pad name="P$123" x="23" y="-5" drill="0.9" diameter="1.27"/>
<pad name="P$120" x="23" y="-7" drill="0.9" diameter="1.27"/>
<pad name="P$116" x="23" y="-9" drill="0.9" diameter="1.27"/>
<pad name="P$113" x="23" y="-11" drill="0.9" diameter="1.27"/>
<pad name="P$109" x="23" y="-13" drill="0.9" diameter="1.27"/>
<pad name="P$107" x="23" y="-15" drill="0.9" diameter="1.27"/>
<pad name="P$102" x="23" y="-17" drill="0.9" diameter="1.27"/>
<pad name="P$99" x="23" y="-19" drill="0.9" diameter="1.27"/>
<pad name="P$97" x="23" y="-21" drill="0.9" diameter="1.27"/>
<pad name="P$94" x="23" y="-23" drill="0.9" diameter="1.27"/>
<pad name="P$90" x="23" y="-25" drill="0.9" diameter="1.27"/>
<pad name="GND@1" x="25" y="19" drill="0.9" diameter="1.27"/>
<pad name="P$160" x="25" y="17" drill="0.9" diameter="1.27"/>
<pad name="P$152" x="25" y="15" drill="0.9" diameter="1.27"/>
<pad name="P$150" x="25" y="13" drill="0.9" diameter="1.27"/>
<pad name="P$146" x="25" y="11" drill="0.9" diameter="1.27"/>
<pad name="P$144" x="25" y="9" drill="0.9" diameter="1.27"/>
<pad name="P$139" x="25" y="7" drill="0.9" diameter="1.27"/>
<pad name="P$137" x="25" y="5" drill="0.9" diameter="1.27"/>
<pad name="P$134" x="25" y="3" drill="0.9" diameter="1.27"/>
<pad name="P$132" x="25" y="1" drill="0.9" diameter="1.27"/>
<pad name="P$128" x="25" y="-1" drill="0.9" diameter="1.27"/>
<pad name="GND@3" x="25" y="-3" drill="0.9" diameter="1.27"/>
<pad name="P$126" x="25" y="-5" drill="0.9" diameter="1.27"/>
<pad name="P$122" x="25" y="-7" drill="0.9" diameter="1.27"/>
<pad name="P$119" x="25" y="-9" drill="0.9" diameter="1.27"/>
<pad name="P$115" x="25" y="-11" drill="0.9" diameter="1.27"/>
<pad name="P$112" x="25" y="-13" drill="0.9" diameter="1.27"/>
<pad name="P$108" x="25" y="-15" drill="0.9" diameter="1.27"/>
<pad name="P$106" x="25" y="-17" drill="0.9" diameter="1.27"/>
<pad name="P$100" x="25" y="-19" drill="0.9" diameter="1.27"/>
<pad name="P$98" x="25" y="-21" drill="0.9" diameter="1.27"/>
<pad name="P$96" x="25" y="-23" drill="0.9" diameter="1.27"/>
<pad name="P$93" x="25" y="-25" drill="0.9" diameter="1.27"/>
<wire x1="-27" y1="29" x2="-27" y2="-27" width="0.127" layer="21"/>
<wire x1="-27" y1="-27" x2="25" y2="-27" width="0.127" layer="21"/>
<wire x1="25" y1="-27" x2="25" y2="29" width="0.127" layer="21"/>
<wire x1="24" y1="22" x2="24" y2="28" width="0.127" layer="51"/>
<wire x1="24" y1="28" x2="6" y2="28" width="0.127" layer="51"/>
<wire x1="25" y1="29" x2="-27" y2="29" width="0.127" layer="21"/>
<wire x1="24" y1="22" x2="18" y2="22" width="0.127" layer="51"/>
<wire x1="13" y1="22" x2="6" y2="22" width="0.127" layer="51"/>
<wire x1="6" y1="22" x2="6" y2="28" width="0.127" layer="51"/>
<wire x1="7" y1="27" x2="7" y2="23" width="0.127" layer="51"/>
<wire x1="7" y1="23" x2="13" y2="23" width="0.127" layer="51"/>
<wire x1="13" y1="23" x2="13" y2="22" width="0.127" layer="51"/>
<wire x1="13" y1="22" x2="18" y2="22" width="0.127" layer="51"/>
<wire x1="18" y1="22" x2="18" y2="23" width="0.127" layer="51"/>
<wire x1="18" y1="23" x2="23" y2="23" width="0.127" layer="51"/>
<wire x1="23" y1="23" x2="23" y2="27" width="0.127" layer="51"/>
<wire x1="23" y1="27" x2="7" y2="27" width="0.127" layer="51"/>
<wire x1="-20" y1="-21" x2="-20" y2="-25" width="0.127" layer="51"/>
<wire x1="-20" y1="-25" x2="-10" y2="-25" width="0.127" layer="51"/>
<wire x1="-10" y1="-25" x2="-10" y2="-21" width="0.127" layer="51"/>
<wire x1="-10" y1="-21" x2="-20" y2="-21" width="0.127" layer="51"/>
<circle x="-15" y="-23" radius="1.4142125" width="0.127" layer="51"/>
<wire x1="8" y1="-21" x2="8" y2="-25" width="0.127" layer="51"/>
<wire x1="8" y1="-25" x2="18" y2="-25" width="0.127" layer="51"/>
<wire x1="18" y1="-25" x2="18" y2="-21" width="0.127" layer="51"/>
<wire x1="18" y1="-21" x2="8" y2="-21" width="0.127" layer="51"/>
<circle x="13" y="-23" radius="1.4142125" width="0.127" layer="51"/>
<wire x1="-13.97" y1="15.24" x2="-13.97" y2="-13.97" width="0.127" layer="51"/>
<wire x1="-13.97" y1="-13.97" x2="13.97" y2="-13.97" width="0.127" layer="51"/>
<wire x1="13.97" y1="-13.97" x2="13.97" y2="15.24" width="0.127" layer="51"/>
<wire x1="13.97" y1="15.24" x2="-13.97" y2="15.24" width="0.127" layer="51"/>
</package>
<package name="CORE3S500E-SMT">
<description>&lt;b&gt;Core3S500E&lt;/b&gt;&lt;p&gt;
The Xilinx Spartan 3E FPGA board from WaveShare.</description>
<text x="-18" y="19" size="1.27" layer="25">&gt;NAME</text>
<text x="-18" y="16" size="1.27" layer="27">&gt;VALUE</text>
<wire x1="-27" y1="29" x2="-27" y2="-27" width="0.127" layer="51"/>
<wire x1="-27" y1="-27" x2="25" y2="-27" width="0.127" layer="51"/>
<wire x1="25" y1="-27" x2="25" y2="29" width="0.127" layer="51"/>
<wire x1="24" y1="22" x2="24" y2="28" width="0.127" layer="51"/>
<wire x1="24" y1="28" x2="6" y2="28" width="0.127" layer="51"/>
<wire x1="25" y1="29" x2="-27" y2="29" width="0.127" layer="51"/>
<wire x1="24" y1="22" x2="18" y2="22" width="0.127" layer="51"/>
<wire x1="13" y1="22" x2="6" y2="22" width="0.127" layer="51"/>
<wire x1="6" y1="22" x2="6" y2="28" width="0.127" layer="51"/>
<wire x1="7" y1="27" x2="7" y2="23" width="0.127" layer="51"/>
<wire x1="7" y1="23" x2="13" y2="23" width="0.127" layer="51"/>
<wire x1="13" y1="23" x2="13" y2="22" width="0.127" layer="51"/>
<wire x1="13" y1="22" x2="18" y2="22" width="0.127" layer="51"/>
<wire x1="18" y1="22" x2="18" y2="23" width="0.127" layer="51"/>
<wire x1="18" y1="23" x2="23" y2="23" width="0.127" layer="51"/>
<wire x1="23" y1="23" x2="23" y2="27" width="0.127" layer="51"/>
<wire x1="23" y1="27" x2="7" y2="27" width="0.127" layer="51"/>
<wire x1="-20" y1="-21" x2="-20" y2="-25" width="0.127" layer="51"/>
<wire x1="-20" y1="-25" x2="-10" y2="-25" width="0.127" layer="51"/>
<wire x1="-10" y1="-25" x2="-10" y2="-21" width="0.127" layer="51"/>
<wire x1="-10" y1="-21" x2="-20" y2="-21" width="0.127" layer="51"/>
<circle x="-15" y="-23" radius="1.4142125" width="0.127" layer="51"/>
<wire x1="8" y1="-21" x2="8" y2="-25" width="0.127" layer="51"/>
<wire x1="8" y1="-25" x2="18" y2="-25" width="0.127" layer="51"/>
<wire x1="18" y1="-25" x2="18" y2="-21" width="0.127" layer="51"/>
<wire x1="18" y1="-21" x2="8" y2="-21" width="0.127" layer="51"/>
<circle x="13" y="-23" radius="1.4142125" width="0.127" layer="51"/>
<wire x1="-13.97" y1="15.24" x2="-13.97" y2="-13.97" width="0.127" layer="51"/>
<wire x1="-13.97" y1="-13.97" x2="13.97" y2="-13.97" width="0.127" layer="51"/>
<wire x1="13.97" y1="-13.97" x2="13.97" y2="15.24" width="0.127" layer="51"/>
<wire x1="13.97" y1="15.24" x2="-13.97" y2="15.24" width="0.127" layer="51"/>
<smd name="2" x="-23" y="28.4" dx="2.2" dy="1" layer="1" rot="R90"/>
<smd name="3" x="-23" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-23.625" y1="26.375" x2="-22.375" y2="27.625" layer="51"/>
<rectangle x1="-23.625" y1="24.375" x2="-22.375" y2="25.625" layer="51"/>
<smd name="203" x="-21" y="28.4" dx="2.2" dy="1" layer="1" rot="R90"/>
<smd name="205" x="-21" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-21.625" y1="26.375" x2="-20.375" y2="27.625" layer="51"/>
<rectangle x1="-21.625" y1="24.375" x2="-20.375" y2="25.625" layer="51"/>
<smd name="4" x="-25" y="28.4" dx="2.2" dy="1" layer="1" rot="R90"/>
<smd name="5" x="-25" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-25.625" y1="26.375" x2="-24.375" y2="27.625" layer="51"/>
<rectangle x1="-25.625" y1="24.375" x2="-24.375" y2="25.625" layer="51"/>
<smd name="199" x="-17" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-17.625" y1="24.375" x2="-16.375" y2="25.625" layer="51"/>
<smd name="196" x="-15" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-15.625" y1="24.375" x2="-14.375" y2="25.625" layer="51"/>
<smd name="202" x="-19" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-19.625" y1="24.375" x2="-18.375" y2="25.625" layer="51"/>
<smd name="186" x="-9" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-9.625" y1="24.375" x2="-8.375" y2="25.625" layer="51"/>
<smd name="181" x="-7" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-7.625" y1="24.375" x2="-6.375" y2="25.625" layer="51"/>
<smd name="189" x="-11" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-11.625" y1="24.375" x2="-10.375" y2="25.625" layer="51"/>
<smd name="177" x="-3" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-3.625" y1="24.375" x2="-2.375" y2="25.625" layer="51"/>
<smd name="171" x="-1" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-1.625" y1="24.375" x2="-0.375" y2="25.625" layer="51"/>
<smd name="179" x="-5" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-5.625" y1="24.375" x2="-4.375" y2="25.625" layer="51"/>
<smd name="167" x="1" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="0.375" y1="24.375" x2="1.625" y2="25.625" layer="51"/>
<smd name="164" x="3" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="2.375" y1="24.375" x2="3.625" y2="25.625" layer="51"/>
<smd name="192" x="-13" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="-13.625" y1="24.375" x2="-12.375" y2="25.625" layer="51"/>
<smd name="162" x="5" y="23.6" dx="2.2" dy="1" layer="1" rot="R90"/>
<rectangle x1="4.375" y1="24.375" x2="5.625" y2="25.625" layer="51"/>
<smd name="163" x="3" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="2.375" y1="26.375" x2="3.625" y2="27.625" layer="51" rot="R180"/>
<smd name="165" x="1" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="0.375" y1="26.375" x2="1.625" y2="27.625" layer="51" rot="R180"/>
<smd name="161" x="5" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="4.375" y1="26.375" x2="5.625" y2="27.625" layer="51" rot="R180"/>
<smd name="172" x="-3" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-3.625" y1="26.375" x2="-2.375" y2="27.625" layer="51" rot="R180"/>
<smd name="178" x="-5" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-5.625" y1="26.375" x2="-4.375" y2="27.625" layer="51" rot="R180"/>
<smd name="168" x="-1" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-1.625" y1="26.375" x2="-0.375" y2="27.625" layer="51" rot="R180"/>
<smd name="185" x="-9" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-9.625" y1="26.375" x2="-8.375" y2="27.625" layer="51" rot="R180"/>
<smd name="187" x="-11" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-11.625" y1="26.375" x2="-10.375" y2="27.625" layer="51" rot="R180"/>
<smd name="180" x="-7" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-7.625" y1="26.375" x2="-6.375" y2="27.625" layer="51" rot="R180"/>
<smd name="190" x="-13" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-13.625" y1="26.375" x2="-12.375" y2="27.625" layer="51" rot="R180"/>
<smd name="193" x="-15" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-15.625" y1="26.375" x2="-14.375" y2="27.625" layer="51" rot="R180"/>
<smd name="200" x="-19" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-19.625" y1="26.375" x2="-18.375" y2="27.625" layer="51" rot="R180"/>
<smd name="197" x="-17" y="28.4" dx="2.2" dy="1" layer="1" rot="R270"/>
<rectangle x1="-17.625" y1="26.375" x2="-16.375" y2="27.625" layer="51" rot="R180"/>
<smd name="47" x="-21.6" y="-9" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-9.625" x2="-22.375" y2="-8.375" layer="51" rot="R90"/>
<smd name="42" x="-21.6" y="-7" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-7.625" x2="-22.375" y2="-6.375" layer="51" rot="R90"/>
<smd name="49" x="-21.6" y="-11" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-11.625" x2="-22.375" y2="-10.375" layer="51" rot="R90"/>
<smd name="5V@2" x="-21.6" y="-3" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-3.625" x2="-22.375" y2="-2.375" layer="51" rot="R90"/>
<smd name="36" x="-21.6" y="-1" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-1.625" x2="-22.375" y2="-0.375" layer="51" rot="R90"/>
<smd name="40" x="-21.6" y="-5" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-5.625" x2="-22.375" y2="-4.375" layer="51" rot="R90"/>
<smd name="31" x="-21.6" y="3" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="2.375" x2="-22.375" y2="3.625" layer="51" rot="R90"/>
<smd name="29" x="-21.6" y="5" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="4.375" x2="-22.375" y2="5.625" layer="51" rot="R90"/>
<smd name="34" x="-21.6" y="1" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="0.375" x2="-22.375" y2="1.625" layer="51" rot="R90"/>
<smd name="23" x="-21.6" y="9" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="8.375" x2="-22.375" y2="9.625" layer="51" rot="R90"/>
<smd name="19" x="-21.6" y="11" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="10.375" x2="-22.375" y2="11.625" layer="51" rot="R90"/>
<smd name="25" x="-21.6" y="7" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="6.375" x2="-22.375" y2="7.625" layer="51" rot="R90"/>
<smd name="16" x="-21.6" y="13" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="12.375" x2="-22.375" y2="13.625" layer="51" rot="R90"/>
<smd name="12" x="-21.6" y="15" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="14.375" x2="-22.375" y2="15.625" layer="51" rot="R90"/>
<smd name="3,3V@2" x="-21.6" y="19" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="18.375" x2="-22.375" y2="19.625" layer="51" rot="R90"/>
<smd name="9" x="-21.6" y="17" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="16.375" x2="-22.375" y2="17.625" layer="51" rot="R90"/>
<smd name="76" x="-21.6" y="-23" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-23.625" x2="-22.375" y2="-22.375" layer="51" rot="R90"/>
<smd name="74" x="-21.6" y="-21" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-21.625" x2="-22.375" y2="-20.375" layer="51" rot="R90"/>
<smd name="82" x="-21.6" y="-25" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-25.625" x2="-22.375" y2="-24.375" layer="51" rot="R90"/>
<smd name="63" x="-21.6" y="-17" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-17.625" x2="-22.375" y2="-16.375" layer="51" rot="R90"/>
<smd name="61" x="-21.6" y="-15" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-15.625" x2="-22.375" y2="-14.375" layer="51" rot="R90"/>
<smd name="65" x="-21.6" y="-19" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-19.625" x2="-22.375" y2="-18.375" layer="51" rot="R90"/>
<smd name="55" x="-21.6" y="-13" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="-23.625" y1="-13.625" x2="-22.375" y2="-12.375" layer="51" rot="R90"/>
<smd name="30" x="-26.4" y="3" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="2.375" x2="-24.375" y2="3.625" layer="51" rot="R270"/>
<smd name="33" x="-26.4" y="1" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="0.375" x2="-24.375" y2="1.625" layer="51" rot="R270"/>
<smd name="28" x="-26.4" y="5" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="4.375" x2="-24.375" y2="5.625" layer="51" rot="R270"/>
<smd name="GND@4" x="-26.4" y="-3" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-3.625" x2="-24.375" y2="-2.375" layer="51" rot="R270"/>
<smd name="39" x="-26.4" y="-5" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-5.625" x2="-24.375" y2="-4.375" layer="51" rot="R270"/>
<smd name="35" x="-26.4" y="-1" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-1.625" x2="-24.375" y2="-0.375" layer="51" rot="R270"/>
<smd name="45" x="-26.4" y="-9" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-9.625" x2="-24.375" y2="-8.375" layer="51" rot="R270"/>
<smd name="48" x="-26.4" y="-11" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-11.625" x2="-24.375" y2="-10.375" layer="51" rot="R270"/>
<smd name="41" x="-26.4" y="-7" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-7.625" x2="-24.375" y2="-6.375" layer="51" rot="R270"/>
<smd name="60" x="-26.4" y="-15" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-15.625" x2="-24.375" y2="-14.375" layer="51" rot="R270"/>
<smd name="62" x="-26.4" y="-17" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-17.625" x2="-24.375" y2="-16.375" layer="51" rot="R270"/>
<smd name="50" x="-26.4" y="-13" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-13.625" x2="-24.375" y2="-12.375" layer="51" rot="R270"/>
<smd name="64" x="-26.4" y="-19" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-19.625" x2="-24.375" y2="-18.375" layer="51" rot="R270"/>
<smd name="69" x="-26.4" y="-21" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-21.625" x2="-24.375" y2="-20.375" layer="51" rot="R270"/>
<smd name="77" x="-26.4" y="-25" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-25.625" x2="-24.375" y2="-24.375" layer="51" rot="R270"/>
<smd name="75" x="-26.4" y="-23" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="-23.625" x2="-24.375" y2="-22.375" layer="51" rot="R270"/>
<smd name="8" x="-26.4" y="17" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="16.375" x2="-24.375" y2="17.625" layer="51" rot="R270"/>
<smd name="11" x="-26.4" y="15" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="14.375" x2="-24.375" y2="15.625" layer="51" rot="R270"/>
<smd name="GND@2" x="-26.4" y="19" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="18.375" x2="-24.375" y2="19.625" layer="51" rot="R270"/>
<smd name="18" x="-26.4" y="11" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="10.375" x2="-24.375" y2="11.625" layer="51" rot="R270"/>
<smd name="22" x="-26.4" y="9" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="8.375" x2="-24.375" y2="9.625" layer="51" rot="R270"/>
<smd name="15" x="-26.4" y="13" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="12.375" x2="-24.375" y2="13.625" layer="51" rot="R270"/>
<smd name="24" x="-26.4" y="7" dx="2.2" dy="1" layer="1"/>
<rectangle x1="-25.625" y1="6.375" x2="-24.375" y2="7.625" layer="51" rot="R270"/>
<smd name="119" x="26.4" y="-9" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-9.625" x2="25.625" y2="-8.375" layer="51" rot="R90"/>
<smd name="122" x="26.4" y="-7" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-7.625" x2="25.625" y2="-6.375" layer="51" rot="R90"/>
<smd name="115" x="26.4" y="-11" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-11.625" x2="25.625" y2="-10.375" layer="51" rot="R90"/>
<smd name="GND@3" x="26.4" y="-3" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-3.625" x2="25.625" y2="-2.375" layer="51" rot="R90"/>
<smd name="128" x="26.4" y="-1" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-1.625" x2="25.625" y2="-0.375" layer="51" rot="R90"/>
<smd name="126" x="26.4" y="-5" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-5.625" x2="25.625" y2="-4.375" layer="51" rot="R90"/>
<smd name="134" x="26.4" y="3" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="2.375" x2="25.625" y2="3.625" layer="51" rot="R90"/>
<smd name="137" x="26.4" y="5" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="4.375" x2="25.625" y2="5.625" layer="51" rot="R90"/>
<smd name="132" x="26.4" y="1" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="0.375" x2="25.625" y2="1.625" layer="51" rot="R90"/>
<smd name="144" x="26.4" y="9" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="8.375" x2="25.625" y2="9.625" layer="51" rot="R90"/>
<smd name="146" x="26.4" y="11" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="10.375" x2="25.625" y2="11.625" layer="51" rot="R90"/>
<smd name="139" x="26.4" y="7" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="6.375" x2="25.625" y2="7.625" layer="51" rot="R90"/>
<smd name="150" x="26.4" y="13" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="12.375" x2="25.625" y2="13.625" layer="51" rot="R90"/>
<smd name="152" x="26.4" y="15" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="14.375" x2="25.625" y2="15.625" layer="51" rot="R90"/>
<smd name="GND@1" x="26.4" y="19" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="18.375" x2="25.625" y2="19.625" layer="51" rot="R90"/>
<smd name="160" x="26.4" y="17" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="16.375" x2="25.625" y2="17.625" layer="51" rot="R90"/>
<smd name="96" x="26.4" y="-23" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-23.625" x2="25.625" y2="-22.375" layer="51" rot="R90"/>
<smd name="98" x="26.4" y="-21" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-21.625" x2="25.625" y2="-20.375" layer="51" rot="R90"/>
<smd name="93" x="26.4" y="-25" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-25.625" x2="25.625" y2="-24.375" layer="51" rot="R90"/>
<smd name="106" x="26.4" y="-17" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-17.625" x2="25.625" y2="-16.375" layer="51" rot="R90"/>
<smd name="108" x="26.4" y="-15" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-15.625" x2="25.625" y2="-14.375" layer="51" rot="R90"/>
<smd name="100" x="26.4" y="-19" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-19.625" x2="25.625" y2="-18.375" layer="51" rot="R90"/>
<smd name="112" x="26.4" y="-13" dx="2.2" dy="1" layer="1" rot="R180"/>
<rectangle x1="24.375" y1="-13.625" x2="25.625" y2="-12.375" layer="51" rot="R90"/>
<smd name="133" x="21.6" y="3" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="2.375" x2="23.625" y2="3.625" layer="51" rot="R270"/>
<smd name="129" x="21.6" y="1" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="0.375" x2="23.625" y2="1.625" layer="51" rot="R270"/>
<smd name="135" x="21.6" y="5" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="4.375" x2="23.625" y2="5.625" layer="51" rot="R270"/>
<smd name="5V@1" x="21.6" y="-3" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-3.625" x2="23.625" y2="-2.375" layer="51" rot="R270"/>
<smd name="123" x="21.6" y="-5" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-5.625" x2="23.625" y2="-4.375" layer="51" rot="R270"/>
<smd name="127" x="21.6" y="-1" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-1.625" x2="23.625" y2="-0.375" layer="51" rot="R270"/>
<smd name="116" x="21.6" y="-9" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-9.625" x2="23.625" y2="-8.375" layer="51" rot="R270"/>
<smd name="113" x="21.6" y="-11" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-11.625" x2="23.625" y2="-10.375" layer="51" rot="R270"/>
<smd name="120" x="21.6" y="-7" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-7.625" x2="23.625" y2="-6.375" layer="51" rot="R270"/>
<smd name="107" x="21.6" y="-15" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-15.625" x2="23.625" y2="-14.375" layer="51" rot="R270"/>
<smd name="102" x="21.6" y="-17" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-17.625" x2="23.625" y2="-16.375" layer="51" rot="R270"/>
<smd name="109" x="21.6" y="-13" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-13.625" x2="23.625" y2="-12.375" layer="51" rot="R270"/>
<smd name="99" x="21.6" y="-19" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-19.625" x2="23.625" y2="-18.375" layer="51" rot="R270"/>
<smd name="97" x="21.6" y="-21" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-21.625" x2="23.625" y2="-20.375" layer="51" rot="R270"/>
<smd name="90" x="21.6" y="-25" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-25.625" x2="23.625" y2="-24.375" layer="51" rot="R270"/>
<smd name="94" x="21.6" y="-23" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="-23.625" x2="23.625" y2="-22.375" layer="51" rot="R270"/>
<smd name="153" x="21.6" y="17" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="16.375" x2="23.625" y2="17.625" layer="51" rot="R270"/>
<smd name="151" x="21.6" y="15" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="14.375" x2="23.625" y2="15.625" layer="51" rot="R270"/>
<smd name="3,3V@1" x="21.6" y="19" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="18.375" x2="23.625" y2="19.625" layer="51" rot="R270"/>
<smd name="145" x="21.6" y="11" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="10.375" x2="23.625" y2="11.625" layer="51" rot="R270"/>
<smd name="140" x="21.6" y="9" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="8.375" x2="23.625" y2="9.625" layer="51" rot="R270"/>
<smd name="147" x="21.6" y="13" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="12.375" x2="23.625" y2="13.625" layer="51" rot="R270"/>
<smd name="138" x="21.6" y="7" dx="2.2" dy="1" layer="1"/>
<rectangle x1="22.375" y1="6.375" x2="23.625" y2="7.625" layer="51" rot="R270"/>
</package>
<package name="MA40">
<description>&lt;b&gt;SPEAKER&lt;/b&gt;</description>
<circle x="0" y="0" radius="1.016" width="0.1524" layer="21"/>
<pad name="-" x="-2.5" y="0" drill="1.016" diameter="1.905"/>
<pad name="+" x="2.5" y="0" drill="1.016" diameter="1.905"/>
<text x="0" y="2" size="1.27" layer="25" ratio="10" align="center">&gt;NAME</text>
<text x="0" y="-2" size="1.27" layer="27" ratio="10" align="center">&gt;VALUE</text>
<circle x="0" y="0" radius="5.05" width="0.127" layer="21"/>
<circle x="0" y="0" radius="4.75" width="0.127" layer="21"/>
</package>
<package name="SOIC127P600X175-8N">
<smd name="1" x="-2.3622" y="1.905" dx="1.9812" dy="0.5588" layer="1"/>
<smd name="2" x="-2.3622" y="0.635" dx="1.9812" dy="0.5588" layer="1"/>
<smd name="3" x="-2.3622" y="-0.635" dx="1.9812" dy="0.5588" layer="1"/>
<smd name="4" x="-2.3622" y="-1.905" dx="1.9812" dy="0.5588" layer="1"/>
<smd name="5" x="2.3622" y="-1.905" dx="1.9812" dy="0.5588" layer="1"/>
<smd name="6" x="2.3622" y="-0.635" dx="1.9812" dy="0.5588" layer="1"/>
<smd name="7" x="2.3622" y="0.635" dx="1.9812" dy="0.5588" layer="1"/>
<smd name="8" x="2.3622" y="1.905" dx="1.9812" dy="0.5588" layer="1"/>
<wire x1="-1.9558" y1="1.651" x2="-1.9558" y2="2.159" width="0.1524" layer="51"/>
<wire x1="-1.9558" y1="2.159" x2="-2.9972" y2="2.159" width="0.1524" layer="51"/>
<wire x1="-2.9972" y1="2.159" x2="-2.9972" y2="1.651" width="0.1524" layer="51"/>
<wire x1="-2.9972" y1="1.651" x2="-1.9558" y2="1.651" width="0.1524" layer="51"/>
<wire x1="-1.9558" y1="0.381" x2="-1.9558" y2="0.889" width="0.1524" layer="51"/>
<wire x1="-1.9558" y1="0.889" x2="-2.9972" y2="0.889" width="0.1524" layer="51"/>
<wire x1="-2.9972" y1="0.889" x2="-2.9972" y2="0.381" width="0.1524" layer="51"/>
<wire x1="-2.9972" y1="0.381" x2="-1.9558" y2="0.381" width="0.1524" layer="51"/>
<wire x1="-1.9558" y1="-0.889" x2="-1.9558" y2="-0.381" width="0.1524" layer="51"/>
<wire x1="-1.9558" y1="-0.381" x2="-2.9972" y2="-0.381" width="0.1524" layer="51"/>
<wire x1="-2.9972" y1="-0.381" x2="-2.9972" y2="-0.889" width="0.1524" layer="51"/>
<wire x1="-2.9972" y1="-0.889" x2="-1.9558" y2="-0.889" width="0.1524" layer="51"/>
<wire x1="-1.9558" y1="-2.159" x2="-1.9558" y2="-1.651" width="0.1524" layer="51"/>
<wire x1="-1.9558" y1="-1.651" x2="-2.9972" y2="-1.651" width="0.1524" layer="51"/>
<wire x1="-2.9972" y1="-1.651" x2="-2.9972" y2="-2.159" width="0.1524" layer="51"/>
<wire x1="-2.9972" y1="-2.159" x2="-1.9558" y2="-2.159" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="-1.651" x2="1.9558" y2="-2.159" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="-2.159" x2="2.9972" y2="-2.159" width="0.1524" layer="51"/>
<wire x1="2.9972" y1="-2.159" x2="2.9972" y2="-1.651" width="0.1524" layer="51"/>
<wire x1="2.9972" y1="-1.651" x2="1.9558" y2="-1.651" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="-0.381" x2="1.9558" y2="-0.889" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="-0.889" x2="2.9972" y2="-0.889" width="0.1524" layer="51"/>
<wire x1="2.9972" y1="-0.889" x2="2.9972" y2="-0.381" width="0.1524" layer="51"/>
<wire x1="2.9972" y1="-0.381" x2="1.9558" y2="-0.381" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="0.889" x2="1.9558" y2="0.381" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="0.381" x2="2.9972" y2="0.381" width="0.1524" layer="51"/>
<wire x1="2.9972" y1="0.381" x2="2.9972" y2="0.889" width="0.1524" layer="51"/>
<wire x1="2.9972" y1="0.889" x2="1.9558" y2="0.889" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="2.159" x2="1.9558" y2="1.651" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="1.651" x2="2.9972" y2="1.651" width="0.1524" layer="51"/>
<wire x1="2.9972" y1="1.651" x2="2.9972" y2="2.159" width="0.1524" layer="51"/>
<wire x1="2.9972" y1="2.159" x2="1.9558" y2="2.159" width="0.1524" layer="51"/>
<wire x1="-1.9558" y1="-2.4384" x2="1.9558" y2="-2.4384" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="-2.4384" x2="1.9558" y2="2.4384" width="0.1524" layer="51"/>
<wire x1="1.9558" y1="2.4384" x2="0.3048" y2="2.4384" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="2.4384" x2="-0.3048" y2="2.4384" width="0.1524" layer="51"/>
<wire x1="-0.3048" y1="2.4384" x2="-1.9558" y2="2.4384" width="0.1524" layer="51"/>
<wire x1="-1.9558" y1="2.4384" x2="-1.9558" y2="-2.4384" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="2.4384" x2="-0.3048" y2="2.4384" width="0" layer="51" curve="-180"/>
<text x="-3.2004" y="2.3368" size="1.27" layer="51" ratio="6" rot="SR0">*</text>
<wire x1="-1.1684" y1="-2.4384" x2="1.1684" y2="-2.4384" width="0.1524" layer="21"/>
<wire x1="1.1684" y1="2.4384" x2="0.3048" y2="2.4384" width="0.1524" layer="21"/>
<wire x1="0.3048" y1="2.4384" x2="-0.3048" y2="2.4384" width="0.1524" layer="21"/>
<wire x1="-0.3048" y1="2.4384" x2="-1.1684" y2="2.4384" width="0.1524" layer="21"/>
<wire x1="0.3048" y1="2.4384" x2="-0.3048" y2="2.4384" width="0" layer="21" curve="-180"/>
<text x="-3.2004" y="2.3368" size="1.27" layer="21" ratio="6" rot="SR0">*</text>
<text x="-4.5212" y="2.8956" size="2.0828" layer="25" ratio="10" rot="SR0">&gt;NAME</text>
<text x="-5.5626" y="-4.9022" size="2.0828" layer="27" ratio="10" rot="SR0">&gt;VALUE</text>
</package>
</packages>
<symbols>
<symbol name="CORE3S500E">
<pin name="4" x="-35.56" y="45.72" length="middle" rot="R270"/>
<pin name="2" x="-33.02" y="45.72" length="middle" rot="R270"/>
<pin name="203" x="-30.48" y="45.72" length="middle" rot="R270"/>
<pin name="200" x="-27.94" y="45.72" length="middle" rot="R270"/>
<pin name="197" x="-25.4" y="45.72" length="middle" rot="R270"/>
<pin name="193" x="-22.86" y="45.72" length="middle" rot="R270"/>
<pin name="190" x="-20.32" y="45.72" length="middle" rot="R270"/>
<pin name="187" x="-17.78" y="45.72" length="middle" rot="R270"/>
<pin name="185" x="-15.24" y="45.72" length="middle" rot="R270"/>
<pin name="180" x="-12.7" y="45.72" length="middle" rot="R270"/>
<pin name="178" x="-10.16" y="45.72" length="middle" rot="R270"/>
<pin name="172" x="-7.62" y="45.72" length="middle" rot="R270"/>
<pin name="168" x="-5.08" y="45.72" length="middle" rot="R270"/>
<pin name="165" x="-2.54" y="45.72" length="middle" rot="R270"/>
<pin name="163" x="0" y="45.72" length="middle" rot="R270"/>
<pin name="161" x="2.54" y="45.72" length="middle" rot="R270"/>
<pin name="5" x="-35.56" y="25.4" length="middle" rot="R90"/>
<pin name="3" x="-33.02" y="25.4" length="middle" rot="R90"/>
<pin name="205" x="-30.48" y="25.4" length="middle" rot="R90"/>
<pin name="202" x="-27.94" y="25.4" length="middle" rot="R90"/>
<pin name="199" x="-25.4" y="25.4" length="middle" rot="R90"/>
<pin name="196" x="-22.86" y="25.4" length="middle" rot="R90"/>
<pin name="192" x="-20.32" y="25.4" length="middle" rot="R90"/>
<pin name="189" x="-17.78" y="25.4" length="middle" rot="R90"/>
<pin name="186" x="-15.24" y="25.4" length="middle" rot="R90"/>
<pin name="181" x="-12.7" y="25.4" length="middle" rot="R90"/>
<pin name="179" x="-10.16" y="25.4" length="middle" rot="R90"/>
<pin name="177" x="-7.62" y="25.4" length="middle" rot="R90"/>
<pin name="171" x="-5.08" y="25.4" length="middle" rot="R90"/>
<pin name="167" x="-2.54" y="25.4" length="middle" rot="R90"/>
<pin name="164" x="0" y="25.4" length="middle" rot="R90"/>
<pin name="162" x="2.54" y="25.4" length="middle" rot="R90"/>
<pin name="GND@1" x="40.64" y="0" length="middle" rot="R180"/>
<pin name="160" x="40.64" y="-2.54" length="middle" rot="R180"/>
<pin name="152" x="40.64" y="-5.08" length="middle" rot="R180"/>
<pin name="150" x="40.64" y="-7.62" length="middle" rot="R180"/>
<pin name="146" x="40.64" y="-10.16" length="middle" rot="R180"/>
<pin name="144" x="40.64" y="-12.7" length="middle" rot="R180"/>
<pin name="139" x="40.64" y="-15.24" length="middle" rot="R180"/>
<pin name="137" x="40.64" y="-17.78" length="middle" rot="R180"/>
<pin name="134" x="40.64" y="-20.32" length="middle" rot="R180"/>
<pin name="132" x="40.64" y="-22.86" length="middle" rot="R180"/>
<pin name="128" x="40.64" y="-25.4" length="middle" rot="R180"/>
<pin name="GND@3" x="40.64" y="-27.94" length="middle" rot="R180"/>
<pin name="126" x="40.64" y="-30.48" length="middle" rot="R180"/>
<pin name="93" x="40.64" y="-55.88" length="middle" rot="R180"/>
<pin name="122" x="40.64" y="-33.02" length="middle" rot="R180"/>
<pin name="119" x="40.64" y="-35.56" length="middle" rot="R180"/>
<pin name="115" x="40.64" y="-38.1" length="middle" rot="R180"/>
<pin name="112" x="40.64" y="-40.64" length="middle" rot="R180"/>
<pin name="108" x="40.64" y="-43.18" length="middle" rot="R180"/>
<pin name="106" x="40.64" y="-45.72" length="middle" rot="R180"/>
<pin name="100" x="40.64" y="-48.26" length="middle" rot="R180"/>
<pin name="98" x="40.64" y="-50.8" length="middle" rot="R180"/>
<pin name="96" x="40.64" y="-53.34" length="middle" rot="R180"/>
<pin name="90" x="17.78" y="-55.88" length="middle"/>
<pin name="94" x="17.78" y="-53.34" length="middle"/>
<pin name="97" x="17.78" y="-50.8" length="middle"/>
<pin name="99" x="17.78" y="-48.26" length="middle"/>
<pin name="102" x="17.78" y="-45.72" length="middle"/>
<pin name="107" x="17.78" y="-43.18" length="middle"/>
<pin name="109" x="17.78" y="-40.64" length="middle"/>
<pin name="113" x="17.78" y="-38.1" length="middle"/>
<pin name="116" x="17.78" y="-35.56" length="middle"/>
<pin name="120" x="17.78" y="-33.02" length="middle"/>
<pin name="123" x="17.78" y="-30.48" length="middle"/>
<pin name="5V@1" x="17.78" y="-27.94" length="middle"/>
<pin name="127" x="17.78" y="-25.4" length="middle"/>
<pin name="129" x="17.78" y="-22.86" length="middle"/>
<pin name="133" x="17.78" y="-20.32" length="middle"/>
<pin name="135" x="17.78" y="-17.78" length="middle"/>
<pin name="138" x="17.78" y="-15.24" length="middle"/>
<pin name="140" x="17.78" y="-12.7" length="middle"/>
<pin name="145" x="17.78" y="-10.16" length="middle"/>
<pin name="147" x="17.78" y="-7.62" length="middle"/>
<pin name="151" x="17.78" y="-5.08" length="middle"/>
<pin name="153" x="17.78" y="-2.54" length="middle"/>
<pin name="3,3V@1" x="17.78" y="0" length="middle"/>
<pin name="3,3V@2" x="-20.32" y="0" length="middle" rot="R180"/>
<pin name="9" x="-20.32" y="-2.54" length="middle" rot="R180"/>
<pin name="12" x="-20.32" y="-5.08" length="middle" rot="R180"/>
<pin name="16" x="-20.32" y="-7.62" length="middle" rot="R180"/>
<pin name="19" x="-20.32" y="-10.16" length="middle" rot="R180"/>
<pin name="23" x="-20.32" y="-12.7" length="middle" rot="R180"/>
<pin name="25" x="-20.32" y="-15.24" length="middle" rot="R180"/>
<pin name="29" x="-20.32" y="-17.78" length="middle" rot="R180"/>
<pin name="31" x="-20.32" y="-20.32" length="middle" rot="R180"/>
<pin name="34" x="-20.32" y="-22.86" length="middle" rot="R180"/>
<pin name="36" x="-20.32" y="-25.4" length="middle" rot="R180"/>
<pin name="5V@2" x="-20.32" y="-27.94" length="middle" rot="R180"/>
<pin name="40" x="-20.32" y="-30.48" length="middle" rot="R180"/>
<pin name="42" x="-20.32" y="-33.02" length="middle" rot="R180"/>
<pin name="47" x="-20.32" y="-35.56" length="middle" rot="R180"/>
<pin name="49" x="-20.32" y="-38.1" length="middle" rot="R180"/>
<pin name="55" x="-20.32" y="-40.64" length="middle" rot="R180"/>
<pin name="61" x="-20.32" y="-43.18" length="middle" rot="R180"/>
<pin name="63" x="-20.32" y="-45.72" length="middle" rot="R180"/>
<pin name="65" x="-20.32" y="-48.26" length="middle" rot="R180"/>
<pin name="74" x="-20.32" y="-50.8" length="middle" rot="R180"/>
<pin name="76" x="-20.32" y="-53.34" length="middle" rot="R180"/>
<pin name="82" x="-20.32" y="-55.88" length="middle" rot="R180"/>
<pin name="77" x="-43.18" y="-55.88" length="middle"/>
<pin name="75" x="-43.18" y="-53.34" length="middle"/>
<pin name="69" x="-43.18" y="-50.8" length="middle"/>
<pin name="64" x="-43.18" y="-48.26" length="middle"/>
<pin name="62" x="-43.18" y="-45.72" length="middle"/>
<pin name="60" x="-43.18" y="-43.18" length="middle"/>
<pin name="50" x="-43.18" y="-40.64" length="middle"/>
<pin name="48" x="-43.18" y="-38.1" length="middle"/>
<pin name="45" x="-43.18" y="-35.56" length="middle"/>
<pin name="41" x="-43.18" y="-33.02" length="middle"/>
<pin name="39" x="-43.18" y="-30.48" length="middle"/>
<pin name="GND@4" x="-43.18" y="-27.94" length="middle"/>
<pin name="35" x="-43.18" y="-25.4" length="middle"/>
<pin name="33" x="-43.18" y="-22.86" length="middle"/>
<pin name="30" x="-43.18" y="-20.32" length="middle"/>
<pin name="28" x="-43.18" y="-17.78" length="middle"/>
<pin name="24" x="-43.18" y="-15.24" length="middle"/>
<pin name="22" x="-43.18" y="-12.7" length="middle"/>
<pin name="18" x="-43.18" y="-10.16" length="middle"/>
<pin name="15" x="-43.18" y="-7.62" length="middle"/>
<pin name="11" x="-43.18" y="-5.08" length="middle"/>
<pin name="8" x="-43.18" y="-2.54" length="middle"/>
<pin name="GND@2" x="-43.18" y="0" length="middle"/>
<wire x1="-38.1" y1="40.64" x2="5.08" y2="40.64" width="0.254" layer="97"/>
<wire x1="5.08" y1="40.64" x2="5.08" y2="30.48" width="0.254" layer="97"/>
<wire x1="5.08" y1="30.48" x2="-38.1" y2="30.48" width="0.254" layer="97"/>
<wire x1="-38.1" y1="30.48" x2="-38.1" y2="40.64" width="0.254" layer="97"/>
<wire x1="-38.1" y1="2.54" x2="-38.1" y2="-58.42" width="0.254" layer="97"/>
<wire x1="-38.1" y1="-58.42" x2="-25.4" y2="-58.42" width="0.254" layer="97"/>
<wire x1="-25.4" y1="-58.42" x2="-25.4" y2="2.54" width="0.254" layer="97"/>
<wire x1="-25.4" y1="2.54" x2="-38.1" y2="2.54" width="0.254" layer="97"/>
<wire x1="22.86" y1="2.54" x2="22.86" y2="-58.42" width="0.254" layer="97"/>
<wire x1="22.86" y1="-58.42" x2="35.56" y2="-58.42" width="0.254" layer="97"/>
<wire x1="35.56" y1="-58.42" x2="35.56" y2="2.54" width="0.254" layer="97"/>
<wire x1="35.56" y1="2.54" x2="22.86" y2="2.54" width="0.254" layer="97"/>
</symbol>
<symbol name="SP">
<wire x1="-1.905" y1="-0.635" x2="1.905" y2="-0.635" width="0.254" layer="94"/>
<wire x1="1.905" y1="-0.635" x2="1.905" y2="0" width="0.254" layer="94"/>
<wire x1="1.905" y1="2.54" x2="-1.905" y2="2.54" width="0.254" layer="94"/>
<wire x1="-1.905" y1="-0.635" x2="-1.905" y2="0" width="0.254" layer="94"/>
<wire x1="1.905" y1="2.54" x2="5.08" y2="5.08" width="0.254" layer="94"/>
<wire x1="5.08" y1="5.08" x2="-5.08" y2="5.08" width="0.254" layer="94"/>
<wire x1="-1.905" y1="2.54" x2="-5.08" y2="5.08" width="0.254" layer="94"/>
<wire x1="2.54" y1="0" x2="1.905" y2="0" width="0.1524" layer="94"/>
<wire x1="1.905" y1="0" x2="1.905" y2="2.54" width="0.254" layer="94"/>
<wire x1="-2.54" y1="0" x2="-1.905" y2="0" width="0.1524" layer="94"/>
<wire x1="-1.905" y1="0" x2="-1.905" y2="2.54" width="0.254" layer="94"/>
<text x="-3.81" y="6.35" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-3.175" size="1.778" layer="96">&gt;VALUE</text>
<pin name="2" x="5.08" y="0" visible="pad" length="short" direction="pas" rot="R180"/>
<pin name="1" x="-5.08" y="0" visible="pad" length="short" direction="pas"/>
</symbol>
<symbol name="TC4427AEOA">
<pin name="IN_A" x="-17.78" y="0" length="middle" direction="in"/>
<pin name="IN_B" x="-17.78" y="-2.54" length="middle" direction="in"/>
<pin name="VDD" x="-17.78" y="-5.08" length="middle" direction="pwr"/>
<pin name="GND" x="-17.78" y="-7.62" length="middle" direction="pas"/>
<pin name="NC_2" x="12.7" y="-7.62" length="middle" direction="nc" rot="R180"/>
<pin name="NC" x="12.7" y="-5.08" length="middle" direction="nc" rot="R180"/>
<pin name="*OUT_B" x="12.7" y="-2.54" length="middle" direction="out" rot="R180"/>
<pin name="*OUT_A" x="12.7" y="0" length="middle" direction="out" rot="R180"/>
<wire x1="-12.7" y1="5.08" x2="-12.7" y2="-12.7" width="0.4064" layer="94"/>
<wire x1="-12.7" y1="-12.7" x2="7.62" y2="-12.7" width="0.4064" layer="94"/>
<wire x1="7.62" y1="-12.7" x2="7.62" y2="5.08" width="0.4064" layer="94"/>
<wire x1="7.62" y1="5.08" x2="-12.7" y2="5.08" width="0.4064" layer="94"/>
<text x="-2.54" y="2.54" size="2.0828" layer="95" ratio="10" rot="SR0" align="center">&gt;NAME</text>
<text x="-2.54" y="-10.16" size="2.0828" layer="96" ratio="10" rot="SR0" align="center">&gt;VALUE</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="CORE3S500E" prefix="DIP">
<description>A Xilinx Spartan 3E FPGA module.</description>
<gates>
<gate name="G$1" symbol="CORE3S500E" x="2.54" y="10.16"/>
</gates>
<devices>
<device name="DIP" package="CORE3S500E">
<connects>
<connect gate="G$1" pin="100" pad="P$100"/>
<connect gate="G$1" pin="102" pad="P$102"/>
<connect gate="G$1" pin="106" pad="P$106"/>
<connect gate="G$1" pin="107" pad="P$107"/>
<connect gate="G$1" pin="108" pad="P$108"/>
<connect gate="G$1" pin="109" pad="P$109"/>
<connect gate="G$1" pin="11" pad="P$11"/>
<connect gate="G$1" pin="112" pad="P$112"/>
<connect gate="G$1" pin="113" pad="P$113"/>
<connect gate="G$1" pin="115" pad="P$115"/>
<connect gate="G$1" pin="116" pad="P$116"/>
<connect gate="G$1" pin="119" pad="P$119"/>
<connect gate="G$1" pin="12" pad="P$12"/>
<connect gate="G$1" pin="120" pad="P$120"/>
<connect gate="G$1" pin="122" pad="P$122"/>
<connect gate="G$1" pin="123" pad="P$123"/>
<connect gate="G$1" pin="126" pad="P$126"/>
<connect gate="G$1" pin="127" pad="P$127"/>
<connect gate="G$1" pin="128" pad="P$128"/>
<connect gate="G$1" pin="129" pad="P$129"/>
<connect gate="G$1" pin="132" pad="P$132"/>
<connect gate="G$1" pin="133" pad="P$133"/>
<connect gate="G$1" pin="134" pad="P$134"/>
<connect gate="G$1" pin="135" pad="P$135"/>
<connect gate="G$1" pin="137" pad="P$137"/>
<connect gate="G$1" pin="138" pad="P$138"/>
<connect gate="G$1" pin="139" pad="P$139"/>
<connect gate="G$1" pin="140" pad="P$140"/>
<connect gate="G$1" pin="144" pad="P$144"/>
<connect gate="G$1" pin="145" pad="P$145"/>
<connect gate="G$1" pin="146" pad="P$146"/>
<connect gate="G$1" pin="147" pad="P$147"/>
<connect gate="G$1" pin="15" pad="P$15"/>
<connect gate="G$1" pin="150" pad="P$150"/>
<connect gate="G$1" pin="151" pad="P$151"/>
<connect gate="G$1" pin="152" pad="P$152"/>
<connect gate="G$1" pin="153" pad="P$153"/>
<connect gate="G$1" pin="16" pad="P$16"/>
<connect gate="G$1" pin="160" pad="P$160"/>
<connect gate="G$1" pin="161" pad="P$161"/>
<connect gate="G$1" pin="162" pad="P$162"/>
<connect gate="G$1" pin="163" pad="P$163"/>
<connect gate="G$1" pin="164" pad="P$164"/>
<connect gate="G$1" pin="165" pad="P$165"/>
<connect gate="G$1" pin="167" pad="P$167"/>
<connect gate="G$1" pin="168" pad="P$168"/>
<connect gate="G$1" pin="171" pad="P$171"/>
<connect gate="G$1" pin="172" pad="P$172"/>
<connect gate="G$1" pin="177" pad="P$177"/>
<connect gate="G$1" pin="178" pad="P$178"/>
<connect gate="G$1" pin="179" pad="P$179"/>
<connect gate="G$1" pin="18" pad="P$18"/>
<connect gate="G$1" pin="180" pad="P$180"/>
<connect gate="G$1" pin="181" pad="P$181"/>
<connect gate="G$1" pin="185" pad="P$185"/>
<connect gate="G$1" pin="186" pad="P$186"/>
<connect gate="G$1" pin="187" pad="P$187"/>
<connect gate="G$1" pin="189" pad="P$189"/>
<connect gate="G$1" pin="19" pad="P$19"/>
<connect gate="G$1" pin="190" pad="P$190"/>
<connect gate="G$1" pin="192" pad="P$192"/>
<connect gate="G$1" pin="193" pad="P$193"/>
<connect gate="G$1" pin="196" pad="P$196"/>
<connect gate="G$1" pin="197" pad="P$197"/>
<connect gate="G$1" pin="199" pad="P$199"/>
<connect gate="G$1" pin="2" pad="P$2"/>
<connect gate="G$1" pin="200" pad="P$200"/>
<connect gate="G$1" pin="202" pad="P$202"/>
<connect gate="G$1" pin="203" pad="P$203"/>
<connect gate="G$1" pin="205" pad="P$205"/>
<connect gate="G$1" pin="22" pad="P$22"/>
<connect gate="G$1" pin="23" pad="P$23"/>
<connect gate="G$1" pin="24" pad="P$24"/>
<connect gate="G$1" pin="25" pad="P$25"/>
<connect gate="G$1" pin="28" pad="P$28"/>
<connect gate="G$1" pin="29" pad="P$29"/>
<connect gate="G$1" pin="3" pad="P$3"/>
<connect gate="G$1" pin="3,3V@1" pad="3,3V@1"/>
<connect gate="G$1" pin="3,3V@2" pad="3,3V@2"/>
<connect gate="G$1" pin="30" pad="P$30"/>
<connect gate="G$1" pin="31" pad="P$31"/>
<connect gate="G$1" pin="33" pad="P$33"/>
<connect gate="G$1" pin="34" pad="P$34"/>
<connect gate="G$1" pin="35" pad="P$35"/>
<connect gate="G$1" pin="36" pad="P$36"/>
<connect gate="G$1" pin="39" pad="P$39"/>
<connect gate="G$1" pin="4" pad="P$4"/>
<connect gate="G$1" pin="40" pad="P$40"/>
<connect gate="G$1" pin="41" pad="P$41"/>
<connect gate="G$1" pin="42" pad="P$42"/>
<connect gate="G$1" pin="45" pad="P$45"/>
<connect gate="G$1" pin="47" pad="P$47"/>
<connect gate="G$1" pin="48" pad="P$48"/>
<connect gate="G$1" pin="49" pad="P$49"/>
<connect gate="G$1" pin="5" pad="P$5"/>
<connect gate="G$1" pin="50" pad="P$50"/>
<connect gate="G$1" pin="55" pad="P$55"/>
<connect gate="G$1" pin="5V@1" pad="5V@1"/>
<connect gate="G$1" pin="5V@2" pad="5V@2"/>
<connect gate="G$1" pin="60" pad="P$60"/>
<connect gate="G$1" pin="61" pad="P$61"/>
<connect gate="G$1" pin="62" pad="P$62"/>
<connect gate="G$1" pin="63" pad="P$63"/>
<connect gate="G$1" pin="64" pad="P$64"/>
<connect gate="G$1" pin="65" pad="P$65"/>
<connect gate="G$1" pin="69" pad="P$69"/>
<connect gate="G$1" pin="74" pad="P$74"/>
<connect gate="G$1" pin="75" pad="P$75"/>
<connect gate="G$1" pin="76" pad="P$76"/>
<connect gate="G$1" pin="77" pad="P$77"/>
<connect gate="G$1" pin="8" pad="P$8"/>
<connect gate="G$1" pin="82" pad="P$82"/>
<connect gate="G$1" pin="9" pad="P$9"/>
<connect gate="G$1" pin="90" pad="P$90"/>
<connect gate="G$1" pin="93" pad="P$93"/>
<connect gate="G$1" pin="94" pad="P$94"/>
<connect gate="G$1" pin="96" pad="P$96"/>
<connect gate="G$1" pin="97" pad="P$97"/>
<connect gate="G$1" pin="98" pad="P$98"/>
<connect gate="G$1" pin="99" pad="P$99"/>
<connect gate="G$1" pin="GND@1" pad="GND@1"/>
<connect gate="G$1" pin="GND@2" pad="GND@2"/>
<connect gate="G$1" pin="GND@3" pad="GND@3"/>
<connect gate="G$1" pin="GND@4" pad="GND@4"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="SMT" package="CORE3S500E-SMT">
<connects>
<connect gate="G$1" pin="100" pad="100"/>
<connect gate="G$1" pin="102" pad="102"/>
<connect gate="G$1" pin="106" pad="106"/>
<connect gate="G$1" pin="107" pad="107"/>
<connect gate="G$1" pin="108" pad="108"/>
<connect gate="G$1" pin="109" pad="109"/>
<connect gate="G$1" pin="11" pad="11"/>
<connect gate="G$1" pin="112" pad="112"/>
<connect gate="G$1" pin="113" pad="113"/>
<connect gate="G$1" pin="115" pad="115"/>
<connect gate="G$1" pin="116" pad="116"/>
<connect gate="G$1" pin="119" pad="119"/>
<connect gate="G$1" pin="12" pad="12"/>
<connect gate="G$1" pin="120" pad="120"/>
<connect gate="G$1" pin="122" pad="122"/>
<connect gate="G$1" pin="123" pad="123"/>
<connect gate="G$1" pin="126" pad="126"/>
<connect gate="G$1" pin="127" pad="127"/>
<connect gate="G$1" pin="128" pad="128"/>
<connect gate="G$1" pin="129" pad="129"/>
<connect gate="G$1" pin="132" pad="132"/>
<connect gate="G$1" pin="133" pad="133"/>
<connect gate="G$1" pin="134" pad="134"/>
<connect gate="G$1" pin="135" pad="135"/>
<connect gate="G$1" pin="137" pad="137"/>
<connect gate="G$1" pin="138" pad="138"/>
<connect gate="G$1" pin="139" pad="139"/>
<connect gate="G$1" pin="140" pad="140"/>
<connect gate="G$1" pin="144" pad="144"/>
<connect gate="G$1" pin="145" pad="145"/>
<connect gate="G$1" pin="146" pad="146"/>
<connect gate="G$1" pin="147" pad="147"/>
<connect gate="G$1" pin="15" pad="15"/>
<connect gate="G$1" pin="150" pad="150"/>
<connect gate="G$1" pin="151" pad="151"/>
<connect gate="G$1" pin="152" pad="152"/>
<connect gate="G$1" pin="153" pad="153"/>
<connect gate="G$1" pin="16" pad="16"/>
<connect gate="G$1" pin="160" pad="160"/>
<connect gate="G$1" pin="161" pad="161"/>
<connect gate="G$1" pin="162" pad="162"/>
<connect gate="G$1" pin="163" pad="163"/>
<connect gate="G$1" pin="164" pad="164"/>
<connect gate="G$1" pin="165" pad="165"/>
<connect gate="G$1" pin="167" pad="167"/>
<connect gate="G$1" pin="168" pad="168"/>
<connect gate="G$1" pin="171" pad="171"/>
<connect gate="G$1" pin="172" pad="172"/>
<connect gate="G$1" pin="177" pad="177"/>
<connect gate="G$1" pin="178" pad="178"/>
<connect gate="G$1" pin="179" pad="179"/>
<connect gate="G$1" pin="18" pad="18"/>
<connect gate="G$1" pin="180" pad="180"/>
<connect gate="G$1" pin="181" pad="181"/>
<connect gate="G$1" pin="185" pad="185"/>
<connect gate="G$1" pin="186" pad="186"/>
<connect gate="G$1" pin="187" pad="187"/>
<connect gate="G$1" pin="189" pad="189"/>
<connect gate="G$1" pin="19" pad="19"/>
<connect gate="G$1" pin="190" pad="190"/>
<connect gate="G$1" pin="192" pad="192"/>
<connect gate="G$1" pin="193" pad="193"/>
<connect gate="G$1" pin="196" pad="196"/>
<connect gate="G$1" pin="197" pad="197"/>
<connect gate="G$1" pin="199" pad="199"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="200" pad="200"/>
<connect gate="G$1" pin="202" pad="202"/>
<connect gate="G$1" pin="203" pad="203"/>
<connect gate="G$1" pin="205" pad="205"/>
<connect gate="G$1" pin="22" pad="22"/>
<connect gate="G$1" pin="23" pad="23"/>
<connect gate="G$1" pin="24" pad="24"/>
<connect gate="G$1" pin="25" pad="25"/>
<connect gate="G$1" pin="28" pad="28"/>
<connect gate="G$1" pin="29" pad="29"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="3,3V@1" pad="3,3V@1"/>
<connect gate="G$1" pin="3,3V@2" pad="3,3V@2"/>
<connect gate="G$1" pin="30" pad="30"/>
<connect gate="G$1" pin="31" pad="31"/>
<connect gate="G$1" pin="33" pad="33"/>
<connect gate="G$1" pin="34" pad="34"/>
<connect gate="G$1" pin="35" pad="35"/>
<connect gate="G$1" pin="36" pad="36"/>
<connect gate="G$1" pin="39" pad="39"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="40" pad="40"/>
<connect gate="G$1" pin="41" pad="41"/>
<connect gate="G$1" pin="42" pad="42"/>
<connect gate="G$1" pin="45" pad="45"/>
<connect gate="G$1" pin="47" pad="47"/>
<connect gate="G$1" pin="48" pad="48"/>
<connect gate="G$1" pin="49" pad="49"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="50" pad="50"/>
<connect gate="G$1" pin="55" pad="55"/>
<connect gate="G$1" pin="5V@1" pad="5V@1"/>
<connect gate="G$1" pin="5V@2" pad="5V@2"/>
<connect gate="G$1" pin="60" pad="60"/>
<connect gate="G$1" pin="61" pad="61"/>
<connect gate="G$1" pin="62" pad="62"/>
<connect gate="G$1" pin="63" pad="63"/>
<connect gate="G$1" pin="64" pad="64"/>
<connect gate="G$1" pin="65" pad="65"/>
<connect gate="G$1" pin="69" pad="69"/>
<connect gate="G$1" pin="74" pad="74"/>
<connect gate="G$1" pin="75" pad="75"/>
<connect gate="G$1" pin="76" pad="76"/>
<connect gate="G$1" pin="77" pad="77"/>
<connect gate="G$1" pin="8" pad="8"/>
<connect gate="G$1" pin="82" pad="82"/>
<connect gate="G$1" pin="9" pad="9"/>
<connect gate="G$1" pin="90" pad="90"/>
<connect gate="G$1" pin="93" pad="93"/>
<connect gate="G$1" pin="94" pad="94"/>
<connect gate="G$1" pin="96" pad="96"/>
<connect gate="G$1" pin="97" pad="97"/>
<connect gate="G$1" pin="98" pad="98"/>
<connect gate="G$1" pin="99" pad="99"/>
<connect gate="G$1" pin="GND@1" pad="GND@1"/>
<connect gate="G$1" pin="GND@2" pad="GND@2"/>
<connect gate="G$1" pin="GND@3" pad="GND@3"/>
<connect gate="G$1" pin="GND@4" pad="GND@4"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="MA40S4S" prefix="SP">
<description>&lt;b&gt;SPEAKER&lt;/b&gt;&lt;p&gt; Source: Buerklin</description>
<gates>
<gate name="G$1" symbol="SP" x="0" y="0"/>
</gates>
<devices>
<device name="" package="MA40">
<connects>
<connect gate="G$1" pin="1" pad="-"/>
<connect gate="G$1" pin="2" pad="+"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TC4427AEOA" prefix="U">
<description>IC, MOSFET DRIVER, LOW SIDE</description>
<gates>
<gate name="A" symbol="TC4427AEOA" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOIC127P600X175-8N">
<connects>
<connect gate="A" pin="*OUT_A" pad="7"/>
<connect gate="A" pin="*OUT_B" pad="5"/>
<connect gate="A" pin="GND" pad="3"/>
<connect gate="A" pin="IN_A" pad="2"/>
<connect gate="A" pin="IN_B" pad="4"/>
<connect gate="A" pin="NC" pad="8"/>
<connect gate="A" pin="NC_2" pad="1"/>
<connect gate="A" pin="VDD" pad="6"/>
</connects>
<technologies>
<technology name="">
<attribute name="MPN" value="TC4427AEOA" constant="no"/>
<attribute name="OC_FARNELL" value="1292285" constant="no"/>
<attribute name="OC_NEWARK" value="96K4020" constant="no"/>
<attribute name="PACKAGE" value="SOIC-8" constant="no"/>
<attribute name="SUPPLIER" value="Microchip" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply1" urn="urn:adsk.eagle:library:371">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
 GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
 Please keep in mind, that these devices are necessary for the
 automatic wiring of the supply signals.&lt;p&gt;
 The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
 In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
 &lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="GND" urn="urn:adsk.eagle:symbol:26925/1" library_version="1">
<wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94"/>
<text x="-2.54" y="-2.54" size="1.778" layer="96">&gt;VALUE</text>
<pin name="GND" x="0" y="2.54" visible="off" length="short" direction="sup" rot="R270"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="GND" urn="urn:adsk.eagle:component:26954/1" prefix="GND" library_version="1">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="GND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply2" urn="urn:adsk.eagle:library:372">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
Please keep in mind, that these devices are necessary for the
automatic wiring of the supply signals.&lt;p&gt;
The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="+05V" urn="urn:adsk.eagle:symbol:26987/1" library_version="2">
<wire x1="-0.635" y1="1.27" x2="0.635" y2="1.27" width="0.1524" layer="94"/>
<wire x1="0" y1="0.635" x2="0" y2="1.905" width="0.1524" layer="94"/>
<circle x="0" y="1.27" radius="1.27" width="0.254" layer="94"/>
<text x="-1.905" y="3.175" size="1.778" layer="96">&gt;VALUE</text>
<pin name="+5V" x="0" y="-2.54" visible="off" length="short" direction="sup" rot="R90"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="+5V" urn="urn:adsk.eagle:component:27032/1" prefix="SUPPLY" library_version="2">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="+5V" symbol="+05V" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="DIP1" library="Parts" deviceset="CORE3S500E" device="SMT"/>
<part name="SP1" library="Parts" deviceset="MA40S4S" device=""/>
<part name="SP2" library="Parts" deviceset="MA40S4S" device=""/>
<part name="U1" library="Parts" deviceset="TC4427AEOA" device=""/>
<part name="GND1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND2" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND3" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND4" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND5" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND6" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="SUPPLY1" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="+5V" device=""/>
<part name="SUPPLY2" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="+5V" device=""/>
<part name="SUPPLY3" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="+5V" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="DIP1" gate="G$1" x="53.34" y="40.64"/>
<instance part="SP1" gate="G$1" x="-35.56" y="33.02" rot="MR0"/>
<instance part="SP2" gate="G$1" x="-35.56" y="25.4" rot="R180"/>
<instance part="U1" gate="A" x="-58.42" y="33.02"/>
<instance part="GND1" gate="1" x="-27.94" y="20.32"/>
<instance part="GND2" gate="1" x="-78.74" y="20.32"/>
<instance part="GND3" gate="1" x="2.54" y="40.64" rot="R270"/>
<instance part="GND4" gate="1" x="2.54" y="12.7" rot="R270"/>
<instance part="GND5" gate="1" x="101.6" y="12.7" rot="R90"/>
<instance part="GND6" gate="1" x="101.6" y="40.64" rot="R90"/>
<instance part="SUPPLY1" gate="+5V" x="-81.28" y="27.94" rot="R90"/>
<instance part="SUPPLY2" gate="+5V" x="38.1" y="12.7" rot="R270"/>
<instance part="SUPPLY3" gate="+5V" x="66.04" y="12.7" rot="R90"/>
</instances>
<busses>
</busses>
<nets>
<net name="N$1" class="0">
<segment>
<pinref part="U1" gate="A" pin="*OUT_A"/>
<pinref part="SP1" gate="G$1" pin="2"/>
<wire x1="-45.72" y1="33.02" x2="-40.64" y2="33.02" width="0.1524" layer="91"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="SP1" gate="G$1" pin="1"/>
<wire x1="-30.48" y1="33.02" x2="-27.94" y2="33.02" width="0.1524" layer="91"/>
<wire x1="-27.94" y1="33.02" x2="-27.94" y2="25.4" width="0.1524" layer="91"/>
<pinref part="SP2" gate="G$1" pin="1"/>
<wire x1="-27.94" y1="25.4" x2="-27.94" y2="22.86" width="0.1524" layer="91"/>
<wire x1="-30.48" y1="25.4" x2="-27.94" y2="25.4" width="0.1524" layer="91"/>
<junction x="-27.94" y="25.4"/>
<pinref part="GND1" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="U1" gate="A" pin="GND"/>
<wire x1="-76.2" y1="25.4" x2="-78.74" y2="25.4" width="0.1524" layer="91"/>
<pinref part="GND2" gate="1" pin="GND"/>
<wire x1="-78.74" y1="25.4" x2="-78.74" y2="22.86" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="DIP1" gate="G$1" pin="GND@4"/>
<pinref part="GND4" gate="1" pin="GND"/>
<wire x1="10.16" y1="12.7" x2="5.08" y2="12.7" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="DIP1" gate="G$1" pin="GND@2"/>
<pinref part="GND3" gate="1" pin="GND"/>
<wire x1="10.16" y1="40.64" x2="5.08" y2="40.64" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="DIP1" gate="G$1" pin="GND@1"/>
<pinref part="GND6" gate="1" pin="GND"/>
<wire x1="93.98" y1="40.64" x2="99.06" y2="40.64" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="DIP1" gate="G$1" pin="GND@3"/>
<pinref part="GND5" gate="1" pin="GND"/>
<wire x1="93.98" y1="12.7" x2="99.06" y2="12.7" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="U1" gate="A" pin="*OUT_B"/>
<wire x1="-45.72" y1="30.48" x2="-43.18" y2="30.48" width="0.1524" layer="91"/>
<wire x1="-43.18" y1="30.48" x2="-43.18" y2="25.4" width="0.1524" layer="91"/>
<pinref part="SP2" gate="G$1" pin="2"/>
<wire x1="-43.18" y1="25.4" x2="-40.64" y2="25.4" width="0.1524" layer="91"/>
</segment>
</net>
<net name="+5V" class="0">
<segment>
<pinref part="DIP1" gate="G$1" pin="5V@2"/>
<pinref part="SUPPLY2" gate="+5V" pin="+5V"/>
<wire x1="33.02" y1="12.7" x2="35.56" y2="12.7" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="U1" gate="A" pin="VDD"/>
<pinref part="SUPPLY1" gate="+5V" pin="+5V"/>
<wire x1="-76.2" y1="27.94" x2="-78.74" y2="27.94" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
<compatibility>
<note version="8.2" severity="warning">
Since Version 8.2, EAGLE supports online libraries. The ids
of those online libraries will not be understood (or retained)
with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports URNs for individual library
assets (packages, symbols, and devices). The URNs of those assets
will not be understood (or retained) with this version.
</note>
</compatibility>
</eagle>
