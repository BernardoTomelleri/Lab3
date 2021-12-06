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
P 8100 2150
F 0 "OA1" H 8300 2250 50  0000 L CNN
F 1 "TL081" H 8300 2350 50  0000 L CNN
F 2 "" H 8150 2200 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 8250 2300 50  0001 C CNN
	1    8100 2150
	1    0    0    1   
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 619ABFCB
P 8000 1850
F 0 "#PWR?" H 8000 1700 50  0001 C CNN
F 1 "+5V" H 8015 2023 50  0000 C CNN
F 2 "" H 8000 1850 50  0001 C CNN
F 3 "" H 8000 1850 50  0001 C CNN
	1    8000 1850
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 619AC645
P 9800 1950
F 0 "#PWR?" H 9800 1800 50  0001 C CNN
F 1 "+5V" H 9815 2123 50  0000 C CNN
F 2 "" H 9800 1950 50  0001 C CNN
F 3 "" H 9800 1950 50  0001 C CNN
	1    9800 1950
	1    0    0    -1  
$EndComp
$Comp
L power:-5V #PWR?
U 1 1 619ACC44
P 8000 2450
F 0 "#PWR?" H 8000 2550 50  0001 C CNN
F 1 "-5V" H 8015 2623 50  0000 C CNN
F 2 "" H 8000 2450 50  0001 C CNN
F 3 "" H 8000 2450 50  0001 C CNN
	1    8000 2450
	-1   0    0    1   
$EndComp
$Comp
L power:-5V #PWR?
U 1 1 619AD451
P 9800 2550
F 0 "#PWR?" H 9800 2650 50  0001 C CNN
F 1 "-5V" H 9815 2723 50  0000 C CNN
F 2 "" H 9800 2550 50  0001 C CNN
F 3 "" H 9800 2550 50  0001 C CNN
	1    9800 2550
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 619AE02E
P 6800 2750
F 0 "#PWR?" H 6800 2500 50  0001 C CNN
F 1 "GND" H 6805 2577 50  0000 C CNN
F 2 "" H 6800 2750 50  0001 C CNN
F 3 "" H 6800 2750 50  0001 C CNN
	1    6800 2750
	1    0    0    -1  
$EndComp
$Comp
L Simulation_SPICE:VPULSE Vs
U 1 1 619AF789
P 6800 2400
F 0 "Vs" H 6930 2446 50  0000 L CNN
F 1 "SQW 100Hz" H 6930 2355 50  0000 L CNN
F 2 "" H 6800 2400 50  0001 C CNN
F 3 "~" H 6800 2400 50  0001 C CNN
F 4 "Y" H 6800 2400 50  0001 L CNN "Spice_Netlist_Enabled"
F 5 "V" H 6800 2400 50  0001 L CNN "Spice_Primitive"
F 6 "sin(0 1 1k)" H 6930 2309 50  0001 L CNN "Spice_Model"
	1    6800 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:C CT
U 1 1 619B1704
P 7200 2050
F 0 "CT" V 6948 2050 50  0000 C CNN
F 1 "1 nF" V 7039 2050 50  0000 C CNN
F 2 "" H 7238 1900 50  0001 C CNN
F 3 "~" H 7200 2050 50  0001 C CNN
	1    7200 2050
	0    1    1    0   
$EndComp
$Comp
L Device:C CF
U 1 1 619B1C2A
P 8100 1000
F 0 "CF" V 7848 1000 50  0000 C CNN
F 1 "1 nF" V 7939 1000 50  0000 C CNN
F 2 "" H 8138 850 50  0001 C CNN
F 3 "~" H 8100 1000 50  0001 C CNN
	1    8100 1000
	0    1    1    0   
$EndComp
Wire Wire Line
	6800 2200 6800 2050
Wire Wire Line
	6800 2050 7050 2050
Wire Wire Line
	7800 2250 7600 2250
Wire Wire Line
	6800 2700 6800 2750
$Comp
L Device:R R1
U 1 1 619C286A
P 8100 1400
F 0 "R1" V 7893 1400 50  0000 C CNN
F 1 "100 k" V 7984 1400 50  0000 C CNN
F 2 "" V 8030 1400 50  0001 C CNN
F 3 "~" H 8100 1400 50  0001 C CNN
	1    8100 1400
	0    1    1    0   
$EndComp
Wire Wire Line
	7650 2050 7650 1400
Wire Wire Line
	7650 1400 7950 1400
Wire Wire Line
	7650 2050 7800 2050
Wire Wire Line
	8400 2150 8550 2150
Wire Wire Line
	8250 1400 8550 1400
Connection ~ 8550 2150
Wire Wire Line
	7650 1400 7650 1000
Wire Wire Line
	7650 1000 7950 1000
Connection ~ 7650 1400
Wire Wire Line
	8250 1000 8550 1000
Wire Wire Line
	8550 1000 8550 1400
Connection ~ 8550 1400
$Comp
L Simulation_SPICE:VDC Vthr
U 1 1 619CC7DC
P 9100 2550
F 0 "Vthr" H 9230 2641 50  0000 L CNN
F 1 "60 mV" H 9230 2550 50  0000 L CNN
F 2 "" H 9100 2550 50  0001 C CNN
F 3 "~" H 9100 2550 50  0001 C CNN
F 4 "Y" H 9100 2550 50  0001 L CNN "Spice_Netlist_Enabled"
F 5 "V" H 9100 2550 50  0001 L CNN "Spice_Primitive"
F 6 "dc(1)" H 9230 2459 50  0001 L CNN "Spice_Model"
	1    9100 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	6800 2600 6800 2700
Connection ~ 6800 2700
Wire Wire Line
	7600 2250 7600 2700
Text GLabel 10450 2250 2    50   Output ~ 0
Vdiscr
Wire Wire Line
	10200 2250 10450 2250
Text GLabel 8600 2250 2    50   BiDi ~ 0
Vsh
Wire Wire Line
	8550 1400 8550 2150
Wire Wire Line
	8550 2150 8550 2250
Wire Wire Line
	8550 2250 8600 2250
Wire Notes Line
	7400 3000 6550 3000
Wire Notes Line
	6550 3000 6550 1700
Wire Notes Line
	6550 1700 7400 1700
Wire Notes Line
	7400 1700 7400 3000
Wire Wire Line
	7350 2050 7650 2050
Connection ~ 7650 2050
Wire Wire Line
	6800 2700 7600 2700
Wire Notes Line
	7500 3000 7500 650 
Wire Notes Line
	8850 650  8850 3000
Wire Notes Line
	8850 3000 7500 3000
Wire Notes Line
	7500 650  8850 650 
Wire Notes Line
	8950 1400 8950 3000
Wire Notes Line
	8950 3000 10350 3000
Wire Notes Line
	10350 3000 10350 1400
Wire Notes Line
	10350 1400 8950 1400
$Comp
L Amplifier_Operational:TL081 OA2
U 1 1 619A99DE
P 9900 2250
F 0 "OA2" H 10050 2500 50  0000 L CNN
F 1 "TL081" H 10050 2400 50  0000 L CNN
F 2 "" H 9950 2300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 10050 2400 50  0001 C CNN
	1    9900 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	8550 2150 9600 2150
Wire Wire Line
	7600 2700 9000 2700
Wire Wire Line
	9000 2700 9000 2750
Wire Wire Line
	9000 2750 9100 2750
Connection ~ 7600 2700
Wire Wire Line
	9100 2350 9600 2350
Text Notes 6700 3100 0    50   ~ 0
Charge injector\n
Text Notes 7900 3100 0    50   ~ 0
Signal shaper
Text Notes 9450 3100 0    50   ~ 0
Comparator
$Comp
L Amplifier_Operational:TL081 OA1
U 1 1 619FAC5D
P 1850 2450
F 0 "OA1" H 2050 2550 50  0000 L CNN
F 1 "TL081" H 2050 2650 50  0000 L CNN
F 2 "" H 1900 2500 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 2000 2600 50  0001 C CNN
	1    1850 2450
	1    0    0    1   
$EndComp
$Comp
L power:-5V #PWR?
U 1 1 619FAEB1
P 1750 2750
F 0 "#PWR?" H 1750 2850 50  0001 C CNN
F 1 "-5V" H 1765 2923 50  0000 C CNN
F 2 "" H 1750 2750 50  0001 C CNN
F 3 "" H 1750 2750 50  0001 C CNN
	1    1750 2750
	-1   0    0    1   
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 619FAEBB
P 1750 2150
F 0 "#PWR?" H 1750 2000 50  0001 C CNN
F 1 "+5V" H 1765 2323 50  0000 C CNN
F 2 "" H 1750 2150 50  0001 C CNN
F 3 "" H 1750 2150 50  0001 C CNN
	1    1750 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2150 2450 2400 2450
$Comp
L Device:R R1
U 1 1 619FAEC6
P 2400 2750
F 0 "R1" H 2470 2796 50  0000 L CNN
F 1 "10 k" H 2470 2705 50  0000 L CNN
F 2 "" V 2330 2750 50  0001 C CNN
F 3 "~" H 2400 2750 50  0001 C CNN
	1    2400 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 2450 2400 2600
Wire Wire Line
	2400 2450 2600 2450
Connection ~ 2400 2450
Text GLabel 2600 2450 2    50   Output ~ 0
Vout
$Comp
L Device:C C1
U 1 1 61AE536E
P 2400 3050
F 0 "C1" H 2550 3100 50  0000 L CNN
F 1 "10 nF" H 2550 3000 50  0000 L CNN
F 2 "" H 2438 2900 50  0001 C CNN
F 3 "~" H 2400 3050 50  0001 C CNN
	1    2400 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 3650 1950 3700
Connection ~ 1950 3700
Wire Wire Line
	2400 3700 1950 3700
$Comp
L power:GND #PWR?
U 1 1 619FAEDB
P 1950 3700
F 0 "#PWR?" H 1950 3450 50  0001 C CNN
F 1 "GND" H 1955 3527 50  0000 C CNN
F 2 "" H 1950 3700 50  0001 C CNN
F 3 "" H 1950 3700 50  0001 C CNN
	1    1950 3700
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 61AE83BC
P 2400 3500
F 0 "C2" H 2550 3550 50  0000 L CNN
F 1 "10 nF" H 2550 3450 50  0000 L CNN
F 2 "" H 2438 3350 50  0001 C CNN
F 3 "~" H 2400 3500 50  0001 C CNN
	1    2400 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 3650 2400 3700
Wire Wire Line
	2400 3200 2400 3300
$Comp
L Device:R R2
U 1 1 619FAED0
P 1950 3500
F 0 "R2" H 2020 3546 50  0000 L CNN
F 1 "10 k" H 2020 3455 50  0000 L CNN
F 2 "" V 1880 3500 50  0001 C CNN
F 3 "~" H 1950 3500 50  0001 C CNN
	1    1950 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 3350 1950 3300
Wire Wire Line
	1950 3300 2400 3300
Connection ~ 2400 3300
Wire Wire Line
	2400 3300 2400 3350
Text GLabel 2600 3300 2    50   Output ~ 0
A
Wire Wire Line
	2400 3300 2600 3300
$Comp
L power:GND #PWR?
U 1 1 61B0D2EF
P 1450 2950
F 0 "#PWR?" H 1450 2700 50  0001 C CNN
F 1 "GND" H 1455 2777 50  0000 C CNN
F 2 "" H 1450 2950 50  0001 C CNN
F 3 "" H 1450 2950 50  0001 C CNN
	1    1450 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 1150 2250 1500
$Comp
L Diode:1N4007 D1
U 1 1 61AE8D85
P 1950 1150
F 0 "D1" H 1950 1367 50  0000 C CNN
F 1 "1N4007" H 1950 1276 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 1950 975 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 1950 1150 50  0001 C CNN
	1    1950 1150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 619FAEF4
P 1950 1500
F 0 "R3" V 1743 1500 50  0000 C CNN
F 1 "10 k" V 1834 1500 50  0000 C CNN
F 2 "" V 1880 1500 50  0001 C CNN
F 3 "~" H 1950 1500 50  0001 C CNN
	1    1950 1500
	0    1    1    0   
$EndComp
$Comp
L Diode:1N4007 D1
U 1 1 61AE95E4
P 1950 1700
F 0 "D1" H 1950 1917 50  0000 C CNN
F 1 "1N4007" H 1950 1826 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 1950 1525 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 1950 1700 50  0001 C CNN
	1    1950 1700
	-1   0    0    1   
$EndComp
Wire Wire Line
	2250 1500 2100 1500
$Comp
L Device:R R4
U 1 1 61B423D9
P 1300 1500
F 0 "R4" V 1093 1500 50  0000 C CNN
F 1 "10 k" V 1184 1500 50  0000 C CNN
F 2 "" V 1230 1500 50  0001 C CNN
F 3 "~" H 1300 1500 50  0001 C CNN
	1    1300 1500
	0    1    1    0   
$EndComp
Wire Wire Line
	1550 2550 1450 2550
Wire Wire Line
	2250 1150 2100 1150
Wire Wire Line
	2400 2450 2400 1500
Wire Wire Line
	2400 1500 2250 1500
Connection ~ 2250 1500
Wire Wire Line
	2100 1700 2250 1700
Wire Wire Line
	2250 1700 2250 1500
Wire Wire Line
	1150 1500 1000 1500
Wire Wire Line
	1800 1150 1650 1150
Wire Wire Line
	1650 1150 1650 1500
Wire Wire Line
	1650 1500 1800 1500
Wire Wire Line
	1800 1700 1650 1700
Wire Wire Line
	1650 1700 1650 1500
Connection ~ 1650 1500
Wire Wire Line
	1650 1500 1450 1500
$Comp
L Device:R_POT POT1
U 1 1 61B65305
P 1000 2350
F 0 "POT1" H 930 2396 50  0000 R CNN
F 1 "10 k" H 930 2305 50  0000 R CNN
F 2 "" H 1000 2350 50  0001 C CNN
F 3 "~" H 1000 2350 50  0001 C CNN
	1    1000 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1550 2350 1150 2350
Wire Wire Line
	1000 2200 1000 1500
$Comp
L Device:R R5
U 1 1 61B680D9
P 1000 3200
F 0 "R5" H 1070 3246 50  0000 L CNN
F 1 "10 k" H 1070 3155 50  0000 L CNN
F 2 "" V 930 3200 50  0001 C CNN
F 3 "~" H 1000 3200 50  0001 C CNN
	1    1000 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1000 2500 1000 3050
Wire Wire Line
	1000 3350 1000 3700
Wire Wire Line
	1000 3700 1950 3700
$Comp
L Amplifier_Operational:TL081 OA1
U 1 1 61B6D167
P 4650 2450
F 0 "OA1" H 4850 2550 50  0000 L CNN
F 1 "TL081" H 4850 2650 50  0000 L CNN
F 2 "" H 4700 2500 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 4800 2600 50  0001 C CNN
	1    4650 2450
	1    0    0    1   
$EndComp
$Comp
L power:-5V #PWR?
U 1 1 61B6D3F5
P 4550 2750
F 0 "#PWR?" H 4550 2850 50  0001 C CNN
F 1 "-5V" H 4565 2923 50  0000 C CNN
F 2 "" H 4550 2750 50  0001 C CNN
F 3 "" H 4550 2750 50  0001 C CNN
	1    4550 2750
	-1   0    0    1   
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 61B6D3FF
P 4550 2150
F 0 "#PWR?" H 4550 2000 50  0001 C CNN
F 1 "+5V" H 4565 2323 50  0000 C CNN
F 2 "" H 4550 2150 50  0001 C CNN
F 3 "" H 4550 2150 50  0001 C CNN
	1    4550 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 2450 5200 2450
$Comp
L Device:R R1
U 1 1 61B6D40A
P 5200 2750
F 0 "R1" H 5270 2796 50  0000 L CNN
F 1 "10 k" H 5270 2705 50  0000 L CNN
F 2 "" V 5130 2750 50  0001 C CNN
F 3 "~" H 5200 2750 50  0001 C CNN
	1    5200 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5200 2450 5200 2600
Wire Wire Line
	5200 2450 5400 2450
Connection ~ 5200 2450
Text GLabel 5400 2450 2    50   Output ~ 0
Vout
$Comp
L Device:C C1
U 1 1 61B6D418
P 5200 3050
F 0 "C1" H 5350 3100 50  0000 L CNN
F 1 "10 nF" H 5350 3000 50  0000 L CNN
F 2 "" H 5238 2900 50  0001 C CNN
F 3 "~" H 5200 3050 50  0001 C CNN
	1    5200 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	4750 3650 4750 3700
Connection ~ 4750 3700
Wire Wire Line
	5200 3700 4750 3700
$Comp
L power:GND #PWR?
U 1 1 61B6D425
P 4750 3700
F 0 "#PWR?" H 4750 3450 50  0001 C CNN
F 1 "GND" H 4755 3527 50  0000 C CNN
F 2 "" H 4750 3700 50  0001 C CNN
F 3 "" H 4750 3700 50  0001 C CNN
	1    4750 3700
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 61B6D42F
P 5200 3500
F 0 "C2" H 5350 3550 50  0000 L CNN
F 1 "10 nF" H 5350 3450 50  0000 L CNN
F 2 "" H 5238 3350 50  0001 C CNN
F 3 "~" H 5200 3500 50  0001 C CNN
	1    5200 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5200 3650 5200 3700
Wire Wire Line
	5200 3200 5200 3300
$Comp
L Device:R R2
U 1 1 61B6D43B
P 4750 3500
F 0 "R2" H 4820 3546 50  0000 L CNN
F 1 "10 k" H 4820 3455 50  0000 L CNN
F 2 "" V 4680 3500 50  0001 C CNN
F 3 "~" H 4750 3500 50  0001 C CNN
	1    4750 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4750 3350 4750 3300
Wire Wire Line
	4750 3300 5200 3300
Connection ~ 5200 3300
Wire Wire Line
	5200 3300 5200 3350
Text GLabel 5400 3300 2    50   Output ~ 0
A
Wire Wire Line
	5200 3300 5400 3300
Wire Wire Line
	5050 1150 5050 1500
$Comp
L Diode:1N4007 D1
U 1 1 61B6D463
P 4750 1150
F 0 "D1" H 4750 1367 50  0000 C CNN
F 1 "1N4007" H 4750 1276 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 4750 975 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 4750 1150 50  0001 C CNN
	1    4750 1150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 61B6D46D
P 4750 1500
F 0 "R3" V 4543 1500 50  0000 C CNN
F 1 "10 k" V 4634 1500 50  0000 C CNN
F 2 "" V 4680 1500 50  0001 C CNN
F 3 "~" H 4750 1500 50  0001 C CNN
	1    4750 1500
	0    1    1    0   
$EndComp
$Comp
L Diode:1N4007 D2
U 1 1 61B6D477
P 4750 1700
F 0 "D2" H 4750 1917 50  0000 C CNN
F 1 "1N4007" H 4750 1826 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 4750 1525 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 4750 1700 50  0001 C CNN
	1    4750 1700
	-1   0    0    1   
$EndComp
Wire Wire Line
	5050 1500 4900 1500
$Comp
L Device:R R4
U 1 1 61B6D482
P 4100 1500
F 0 "R4" V 3893 1500 50  0000 C CNN
F 1 "10 k" V 3984 1500 50  0000 C CNN
F 2 "" V 4030 1500 50  0001 C CNN
F 3 "~" H 4100 1500 50  0001 C CNN
	1    4100 1500
	0    1    1    0   
$EndComp
Wire Wire Line
	4350 2550 4250 2550
Wire Wire Line
	5050 1150 4900 1150
Wire Wire Line
	5200 2450 5200 1500
Wire Wire Line
	5200 1500 5050 1500
Connection ~ 5050 1500
Wire Wire Line
	4900 1700 5050 1700
Wire Wire Line
	5050 1700 5050 1500
Wire Wire Line
	3950 1500 3800 1500
Wire Wire Line
	4600 1150 4450 1150
Wire Wire Line
	4450 1150 4450 1500
Wire Wire Line
	4450 1500 4600 1500
Wire Wire Line
	4600 1700 4450 1700
Wire Wire Line
	4450 1700 4450 1500
Connection ~ 4450 1500
Wire Wire Line
	4450 1500 4250 1500
$Comp
L Device:R_POT POT1
U 1 1 61B6D49B
P 3800 2350
F 0 "POT1" H 3730 2396 50  0000 R CNN
F 1 "10 k" H 3730 2305 50  0000 R CNN
F 2 "" H 3800 2350 50  0001 C CNN
F 3 "~" H 3800 2350 50  0001 C CNN
	1    3800 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	4350 2350 3950 2350
Wire Wire Line
	3800 2200 3800 1500
$Comp
L Device:R R5
U 1 1 61B6D4A7
P 3800 3200
F 0 "R5" H 3870 3246 50  0000 L CNN
F 1 "10 k" H 3870 3155 50  0000 L CNN
F 2 "" V 3730 3200 50  0001 C CNN
F 3 "~" H 3800 3200 50  0001 C CNN
	1    3800 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 2500 3800 3050
Wire Wire Line
	3800 3350 3800 3700
Wire Wire Line
	3800 3700 4750 3700
Wire Wire Line
	4250 2550 4250 3050
Wire Wire Line
	4250 3050 4750 3050
Wire Wire Line
	4750 3050 4750 3300
Connection ~ 4750 3300
$Comp
L Simulation_SPICE:VSIN Vs
U 1 1 61B0AE31
P 1450 2750
F 0 "Vs" H 1250 2900 50  0000 L CNN
F 1 "VSIN" H 1150 2750 50  0000 L CNN
F 2 "" H 1450 2750 50  0001 C CNN
F 3 "~" H 1450 2750 50  0001 C CNN
F 4 "Y" H 1450 2750 50  0001 L CNN "Spice_Netlist_Enabled"
F 5 "V" H 1450 2750 50  0001 L CNN "Spice_Primitive"
F 6 "sin(0 1 1k)" H 1150 2600 50  0001 L CNN "Spice_Model"
	1    1450 2750
	1    0    0    -1  
$EndComp
$EndSCHEMATC
