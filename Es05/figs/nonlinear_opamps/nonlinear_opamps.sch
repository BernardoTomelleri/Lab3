EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Amplifier_Operational:TL081 OA1
U 1 1 619A821B
P 2150 2250
F 0 "OA1" H 2350 2350 50  0000 L CNN
F 1 "TL081" H 2350 2450 50  0000 L CNN
F 2 "" H 2200 2300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 2300 2400 50  0001 C CNN
	1    2150 2250
	1    0    0    1   
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 619ABFCB
P 2050 1950
F 0 "#PWR?" H 2050 1800 50  0001 C CNN
F 1 "+5V" H 2065 2123 50  0000 C CNN
F 2 "" H 2050 1950 50  0001 C CNN
F 3 "" H 2050 1950 50  0001 C CNN
	1    2050 1950
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 619AC645
P 3850 2050
F 0 "#PWR?" H 3850 1900 50  0001 C CNN
F 1 "+5V" H 3865 2223 50  0000 C CNN
F 2 "" H 3850 2050 50  0001 C CNN
F 3 "" H 3850 2050 50  0001 C CNN
	1    3850 2050
	1    0    0    -1  
$EndComp
$Comp
L power:-5V #PWR?
U 1 1 619ACC44
P 2050 2550
F 0 "#PWR?" H 2050 2650 50  0001 C CNN
F 1 "-5V" H 2065 2723 50  0000 C CNN
F 2 "" H 2050 2550 50  0001 C CNN
F 3 "" H 2050 2550 50  0001 C CNN
	1    2050 2550
	-1   0    0    1   
$EndComp
$Comp
L power:-5V #PWR?
U 1 1 619AD451
P 3850 2650
F 0 "#PWR?" H 3850 2750 50  0001 C CNN
F 1 "-5V" H 3865 2823 50  0000 C CNN
F 2 "" H 3850 2650 50  0001 C CNN
F 3 "" H 3850 2650 50  0001 C CNN
	1    3850 2650
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 619AE02E
P 850 2850
F 0 "#PWR?" H 850 2600 50  0001 C CNN
F 1 "GND" H 855 2677 50  0000 C CNN
F 2 "" H 850 2850 50  0001 C CNN
F 3 "" H 850 2850 50  0001 C CNN
	1    850  2850
	1    0    0    -1  
$EndComp
$Comp
L Simulation_SPICE:VPULSE Vs
U 1 1 619AF789
P 850 2500
F 0 "Vs" H 980 2546 50  0000 L CNN
F 1 "SQW 100Hz" H 980 2455 50  0000 L CNN
F 2 "" H 850 2500 50  0001 C CNN
F 3 "~" H 850 2500 50  0001 C CNN
F 4 "Y" H 850 2500 50  0001 L CNN "Spice_Netlist_Enabled"
F 5 "V" H 850 2500 50  0001 L CNN "Spice_Primitive"
F 6 "sin(0 1 1k)" H 980 2409 50  0001 L CNN "Spice_Model"
	1    850  2500
	1    0    0    -1  
$EndComp
$Comp
L Device:C CT
U 1 1 619B1704
P 1250 2150
F 0 "CT" V 998 2150 50  0000 C CNN
F 1 "1 nF" V 1089 2150 50  0000 C CNN
F 2 "" H 1288 2000 50  0001 C CNN
F 3 "~" H 1250 2150 50  0001 C CNN
	1    1250 2150
	0    1    1    0   
$EndComp
$Comp
L Device:C CF
U 1 1 619B1C2A
P 2150 1100
F 0 "CF" V 1898 1100 50  0000 C CNN
F 1 "1 nF" V 1989 1100 50  0000 C CNN
F 2 "" H 2188 950 50  0001 C CNN
F 3 "~" H 2150 1100 50  0001 C CNN
	1    2150 1100
	0    1    1    0   
$EndComp
Wire Wire Line
	850  2300 850  2150
Wire Wire Line
	850  2150 1100 2150
Wire Wire Line
	1850 2350 1650 2350
Wire Wire Line
	850  2800 850  2850
$Comp
L Device:R R1
U 1 1 619C286A
P 2150 1500
F 0 "R1" V 1943 1500 50  0000 C CNN
F 1 "100 k" V 2034 1500 50  0000 C CNN
F 2 "" V 2080 1500 50  0001 C CNN
F 3 "~" H 2150 1500 50  0001 C CNN
	1    2150 1500
	0    1    1    0   
$EndComp
Wire Wire Line
	1700 2150 1700 1500
Wire Wire Line
	1700 1500 2000 1500
Wire Wire Line
	1700 2150 1850 2150
Wire Wire Line
	2450 2250 2600 2250
Wire Wire Line
	2300 1500 2600 1500
Connection ~ 2600 2250
Wire Wire Line
	1700 1500 1700 1100
Wire Wire Line
	1700 1100 2000 1100
Connection ~ 1700 1500
Wire Wire Line
	2300 1100 2600 1100
Wire Wire Line
	2600 1100 2600 1500
Connection ~ 2600 1500
$Comp
L Simulation_SPICE:VDC Vthr
U 1 1 619CC7DC
P 3150 2650
F 0 "Vthr" H 3280 2741 50  0000 L CNN
F 1 "60 mV" H 3280 2650 50  0000 L CNN
F 2 "" H 3150 2650 50  0001 C CNN
F 3 "~" H 3150 2650 50  0001 C CNN
F 4 "Y" H 3150 2650 50  0001 L CNN "Spice_Netlist_Enabled"
F 5 "V" H 3150 2650 50  0001 L CNN "Spice_Primitive"
F 6 "dc(1)" H 3280 2559 50  0001 L CNN "Spice_Model"
	1    3150 2650
	1    0    0    -1  
$EndComp
Wire Wire Line
	850  2700 850  2800
Connection ~ 850  2800
Wire Wire Line
	1650 2350 1650 2800
Text GLabel 4500 2350 2    50   Output ~ 0
Vdiscr
Wire Wire Line
	4250 2350 4500 2350
Text GLabel 2650 2350 2    50   BiDi ~ 0
Vsh
Wire Wire Line
	2600 1500 2600 2250
Wire Wire Line
	2600 2250 2600 2350
Wire Wire Line
	2600 2350 2650 2350
Wire Notes Line
	1450 3100 600  3100
Wire Notes Line
	600  3100 600  1800
Wire Notes Line
	600  1800 1450 1800
Wire Notes Line
	1450 1800 1450 3100
Wire Wire Line
	1400 2150 1700 2150
Connection ~ 1700 2150
Wire Wire Line
	850  2800 1650 2800
Wire Notes Line
	1550 3100 1550 750 
Wire Notes Line
	2900 750  2900 3100
Wire Notes Line
	2900 3100 1550 3100
Wire Notes Line
	1550 750  2900 750 
Wire Notes Line
	3000 1500 3000 3100
Wire Notes Line
	3000 3100 4400 3100
Wire Notes Line
	4400 3100 4400 1500
Wire Notes Line
	4400 1500 3000 1500
$Comp
L Amplifier_Operational:TL081 OA2
U 1 1 619A99DE
P 3950 2350
F 0 "OA2" H 4150 2450 50  0000 L CNN
F 1 "TL081" H 4150 2550 50  0000 L CNN
F 2 "" H 4000 2400 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 4100 2500 50  0001 C CNN
	1    3950 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 2250 3650 2250
Wire Wire Line
	1650 2800 3050 2800
Wire Wire Line
	3050 2800 3050 2850
Wire Wire Line
	3050 2850 3150 2850
Connection ~ 1650 2800
Wire Wire Line
	3150 2450 3650 2450
Text Notes 750  3200 0    50   ~ 0
Charge injector\n
Text Notes 1950 3200 0    50   ~ 0
Signal shaper
Text Notes 3500 3200 0    50   ~ 0
Comparator
$Comp
L Amplifier_Operational:TL081 OA1
U 1 1 619CC235
P 5950 2100
F 0 "OA1" H 6150 2200 50  0000 L CNN
F 1 "TL081" H 6150 2300 50  0000 L CNN
F 2 "" H 6000 2150 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 6100 2250 50  0001 C CNN
	1    5950 2100
	1    0    0    1   
$EndComp
$Comp
L power:-5V #PWR?
U 1 1 619CC241
P 5850 2400
F 0 "#PWR?" H 5850 2500 50  0001 C CNN
F 1 "-5V" H 5865 2573 50  0000 C CNN
F 2 "" H 5850 2400 50  0001 C CNN
F 3 "" H 5850 2400 50  0001 C CNN
	1    5850 2400
	-1   0    0    1   
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 619CC23B
P 5850 1800
F 0 "#PWR?" H 5850 1650 50  0001 C CNN
F 1 "+5V" H 5865 1973 50  0000 C CNN
F 2 "" H 5850 1800 50  0001 C CNN
F 3 "" H 5850 1800 50  0001 C CNN
	1    5850 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	6250 2100 6500 2100
$Comp
L Device:R R1
U 1 1 619D10C2
P 6500 2400
F 0 "R1" H 6570 2446 50  0000 L CNN
F 1 "10 k" H 6570 2355 50  0000 L CNN
F 2 "" V 6430 2400 50  0001 C CNN
F 3 "~" H 6500 2400 50  0001 C CNN
	1    6500 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 619D1648
P 6500 2900
F 0 "R2" H 6570 2946 50  0000 L CNN
F 1 "2.2 k" H 6570 2855 50  0000 L CNN
F 2 "" V 6430 2900 50  0001 C CNN
F 3 "~" H 6500 2900 50  0001 C CNN
	1    6500 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	6500 2100 6500 2250
Wire Wire Line
	5650 2200 5500 2200
Wire Wire Line
	5500 2200 5500 2650
Wire Wire Line
	5500 2650 6500 2650
Wire Wire Line
	6500 2550 6500 2650
Connection ~ 6500 2650
Wire Wire Line
	6500 2650 6500 2750
$Comp
L power:GND #PWR?
U 1 1 619D5D3F
P 6500 3050
F 0 "#PWR?" H 6500 2800 50  0001 C CNN
F 1 "GND" H 6505 2877 50  0000 C CNN
F 2 "" H 6500 3050 50  0001 C CNN
F 3 "" H 6500 3050 50  0001 C CNN
	1    6500 3050
	1    0    0    -1  
$EndComp
Text GLabel 5500 2000 0    50   Input ~ 0
Vin
Wire Wire Line
	5650 2000 5500 2000
Text GLabel 6700 2100 2    50   Output ~ 0
Vout
Wire Wire Line
	6500 2100 6700 2100
Connection ~ 6500 2100
$Comp
L Amplifier_Operational:TL081 OA?
U 1 1 619E48F1
P 8950 2100
F 0 "OA?" H 9150 2200 50  0000 L CNN
F 1 "TL081" H 9150 2300 50  0000 L CNN
F 2 "" H 9000 2150 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 9100 2250 50  0001 C CNN
	1    8950 2100
	1    0    0    1   
$EndComp
$Comp
L power:-5V #PWR?
U 1 1 619E4AA9
P 8850 2400
F 0 "#PWR?" H 8850 2500 50  0001 C CNN
F 1 "-5V" H 8865 2573 50  0000 C CNN
F 2 "" H 8850 2400 50  0001 C CNN
F 3 "" H 8850 2400 50  0001 C CNN
	1    8850 2400
	-1   0    0    1   
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 619E4AB3
P 8850 1800
F 0 "#PWR?" H 8850 1650 50  0001 C CNN
F 1 "+5V" H 8865 1973 50  0000 C CNN
F 2 "" H 8850 1800 50  0001 C CNN
F 3 "" H 8850 1800 50  0001 C CNN
	1    8850 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	9250 2100 9500 2100
$Comp
L Device:R R1
U 1 1 619E4ABE
P 9500 2400
F 0 "R1" H 9570 2446 50  0000 L CNN
F 1 "10 k" H 9570 2355 50  0000 L CNN
F 2 "" V 9430 2400 50  0001 C CNN
F 3 "~" H 9500 2400 50  0001 C CNN
	1    9500 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 619E4AC8
P 9500 2900
F 0 "R2" H 9570 2946 50  0000 L CNN
F 1 "10 k" H 9570 2855 50  0000 L CNN
F 2 "" V 9430 2900 50  0001 C CNN
F 3 "~" H 9500 2900 50  0001 C CNN
	1    9500 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	9500 2100 9500 2250
$Comp
L power:GND #PWR?
U 1 1 619E4AD8
P 9500 3050
F 0 "#PWR?" H 9500 2800 50  0001 C CNN
F 1 "GND" H 9505 2877 50  0000 C CNN
F 2 "" H 9500 3050 50  0001 C CNN
F 3 "" H 9500 3050 50  0001 C CNN
	1    9500 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	9500 2100 9700 2100
Connection ~ 9500 2100
Text GLabel 9700 2100 2    50   Output ~ 0
Vout
Wire Wire Line
	9500 2550 9500 2650
Wire Wire Line
	8650 2200 8550 2200
Wire Wire Line
	8550 2200 8550 2650
Wire Wire Line
	8550 2650 9500 2650
Connection ~ 9500 2650
Wire Wire Line
	9500 2650 9500 2750
Wire Wire Line
	8650 2000 8250 2000
Wire Wire Line
	8250 2000 8250 2300
Wire Wire Line
	8250 2600 8250 3050
Wire Wire Line
	8250 3050 9500 3050
Connection ~ 9500 3050
Wire Wire Line
	9500 2100 9500 1450
$Comp
L Device:R R3
U 1 1 619F5A2D
P 8900 1450
F 0 "R3" V 8693 1450 50  0000 C CNN
F 1 "10 k" V 8784 1450 50  0000 C CNN
F 2 "" V 8830 1450 50  0001 C CNN
F 3 "~" H 8900 1450 50  0001 C CNN
	1    8900 1450
	0    1    1    0   
$EndComp
Wire Wire Line
	8250 1450 8250 2000
Connection ~ 8250 2000
Wire Wire Line
	9500 1450 9050 1450
Wire Wire Line
	8750 1450 8250 1450
$Comp
L Device:C C1
U 1 1 619EBC68
P 8250 2450
F 0 "C1" H 7950 2500 50  0000 L CNN
F 1 "100 nF" H 7850 2400 50  0000 L CNN
F 2 "" H 8288 2300 50  0001 C CNN
F 3 "~" H 8250 2450 50  0001 C CNN
	1    8250 2450
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:TL081 OA?
U 1 1 619FAC5D
P 2700 4650
F 0 "OA?" H 2900 4750 50  0000 L CNN
F 1 "TL081" H 2900 4850 50  0000 L CNN
F 2 "" H 2750 4700 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 2850 4800 50  0001 C CNN
	1    2700 4650
	1    0    0    1   
$EndComp
$Comp
L power:-5V #PWR?
U 1 1 619FAEB1
P 2600 4950
F 0 "#PWR?" H 2600 5050 50  0001 C CNN
F 1 "-5V" H 2615 5123 50  0000 C CNN
F 2 "" H 2600 4950 50  0001 C CNN
F 3 "" H 2600 4950 50  0001 C CNN
	1    2600 4950
	-1   0    0    1   
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 619FAEBB
P 2600 4350
F 0 "#PWR?" H 2600 4200 50  0001 C CNN
F 1 "+5V" H 2615 4523 50  0000 C CNN
F 2 "" H 2600 4350 50  0001 C CNN
F 3 "" H 2600 4350 50  0001 C CNN
	1    2600 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 4650 3250 4650
$Comp
L Device:R R1
U 1 1 619FAEC6
P 3250 4950
F 0 "R1" H 3320 4996 50  0000 L CNN
F 1 "10 k" H 3320 4905 50  0000 L CNN
F 2 "" V 3180 4950 50  0001 C CNN
F 3 "~" H 3250 4950 50  0001 C CNN
	1    3250 4950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 619FAED0
P 3250 5450
F 0 "R2" H 3320 5496 50  0000 L CNN
F 1 "10 k" H 3320 5405 50  0000 L CNN
F 2 "" V 3180 5450 50  0001 C CNN
F 3 "~" H 3250 5450 50  0001 C CNN
	1    3250 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	3250 4650 3250 4800
$Comp
L power:GND #PWR?
U 1 1 619FAEDB
P 3250 5600
F 0 "#PWR?" H 3250 5350 50  0001 C CNN
F 1 "GND" H 3255 5427 50  0000 C CNN
F 2 "" H 3250 5600 50  0001 C CNN
F 3 "" H 3250 5600 50  0001 C CNN
	1    3250 5600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3250 4650 3450 4650
Connection ~ 3250 4650
Text GLabel 3450 4650 2    50   Output ~ 0
Vout
Wire Wire Line
	2400 4750 2300 4750
Wire Wire Line
	2400 4550 2000 4550
Wire Wire Line
	3250 4650 3250 4000
$Comp
L Device:R R3
U 1 1 619FAEF4
P 2650 4000
F 0 "R3" V 2443 4000 50  0000 C CNN
F 1 "10 k" V 2534 4000 50  0000 C CNN
F 2 "" V 2580 4000 50  0001 C CNN
F 3 "~" H 2650 4000 50  0001 C CNN
	1    2650 4000
	0    1    1    0   
$EndComp
Wire Wire Line
	2000 4000 2000 4550
Wire Wire Line
	3250 4000 2800 4000
Wire Wire Line
	2500 4000 2000 4000
$Comp
L Device:C C1
U 1 1 619FAF02
P 2000 4800
F 0 "C1" H 1700 4850 50  0000 L CNN
F 1 "100 nF" H 1600 4750 50  0000 L CNN
F 2 "" H 2038 4650 50  0001 C CNN
F 3 "~" H 2000 4800 50  0001 C CNN
	1    2000 4800
	1    0    0    -1  
$EndComp
Connection ~ 2000 4550
Wire Wire Line
	2000 4550 2000 4650
Wire Wire Line
	2000 4550 1900 4550
Wire Wire Line
	1600 4550 1500 4550
Wire Wire Line
	1500 4550 1500 5000
Wire Wire Line
	1500 5000 1750 5000
Wire Wire Line
	2000 5000 2000 4950
$Comp
L power:GND #PWR?
U 1 1 61A1C396
P 1750 5000
F 0 "#PWR?" H 1750 4750 50  0001 C CNN
F 1 "GND" H 1755 4827 50  0000 C CNN
F 2 "" H 1750 5000 50  0001 C CNN
F 3 "" H 1750 5000 50  0001 C CNN
	1    1750 5000
	1    0    0    -1  
$EndComp
Connection ~ 1750 5000
Wire Wire Line
	1750 5000 2000 5000
Wire Wire Line
	3250 5100 3250 5200
Wire Wire Line
	2300 4750 2300 5500
Wire Wire Line
	2300 5500 2950 5500
Wire Wire Line
	2950 5500 2950 5200
Wire Wire Line
	2950 5200 3250 5200
Connection ~ 3250 5200
Wire Wire Line
	3250 5200 3250 5300
Wire Wire Line
	2300 5500 2250 5500
Connection ~ 2300 5500
$Comp
L Device:C C2
U 1 1 61A21389
P 1700 5500
F 0 "C2" V 1450 5350 50  0000 L CNN
F 1 "1 nF" V 1550 5350 50  0000 L CNN
F 2 "" H 1738 5350 50  0001 C CNN
F 3 "~" H 1700 5500 50  0001 C CNN
	1    1700 5500
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 61A23E09
P 1950 5750
F 0 "R4" H 2020 5796 50  0000 L CNN
F 1 "10 k" H 2020 5705 50  0000 L CNN
F 2 "" V 1880 5750 50  0001 C CNN
F 3 "~" H 1950 5750 50  0001 C CNN
	1    1950 5750
	1    0    0    -1  
$EndComp
$Comp
L Simulation_SPICE:VPULSE Vtrig
U 1 1 61A244CC
P 1500 5750
F 0 "Vtrig" H 950 5800 50  0000 L CNN
F 1 "SQW 100Hz" H 950 5700 50  0000 L CNN
F 2 "" H 1500 5750 50  0001 C CNN
F 3 "~" H 1500 5750 50  0001 C CNN
F 4 "Y" H 1500 5750 50  0001 L CNN "Spice_Netlist_Enabled"
F 5 "V" H 1500 5750 50  0001 L CNN "Spice_Primitive"
F 6 "sin(0 1 1k)" H 1630 5659 50  0001 L CNN "Spice_Model"
	1    1500 5750
	1    0    0    -1  
$EndComp
Wire Wire Line
	1500 5500 1500 5550
Wire Wire Line
	1950 5500 1950 5600
Wire Wire Line
	1950 5900 1950 6000
Wire Wire Line
	1950 6000 1500 6000
Wire Wire Line
	1500 6000 1500 5950
$Comp
L power:GND #PWR?
U 1 1 61A412B4
P 1950 6000
F 0 "#PWR?" H 1950 5750 50  0001 C CNN
F 1 "GND" H 1955 5827 50  0000 C CNN
F 2 "" H 1950 6000 50  0001 C CNN
F 3 "" H 1950 6000 50  0001 C CNN
	1    1950 6000
	1    0    0    -1  
$EndComp
Connection ~ 1950 6000
Wire Wire Line
	1950 5500 1850 5500
Wire Wire Line
	1550 5500 1500 5500
$Comp
L Diode:1N4007 D1
U 1 1 61A49C4E
P 1750 4550
F 0 "D1" H 1750 4767 50  0000 C CNN
F 1 "1N4007" H 1750 4676 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 1750 4375 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 1750 4550 50  0001 C CNN
	1    1750 4550
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4007 D2
U 1 1 61A4B310
P 2100 5500
F 0 "D2" H 2100 5717 50  0000 C CNN
F 1 "1N4007" H 2100 5626 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 2100 5325 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 2100 5500 50  0001 C CNN
	1    2100 5500
	1    0    0    -1  
$EndComp
Connection ~ 1950 5500
$EndSCHEMATC
