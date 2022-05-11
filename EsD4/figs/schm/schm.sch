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
L Device:Microphone_Ultrasound MK1
U 1 1 62090EE7
P 2450 1550
F 0 "MK1" V 2183 1550 50  0000 C CNN
F 1 "Microphone_Ultrasound" V 2274 1550 50  0000 C CNN
F 2 "" V 2500 1480 50  0001 L CNN
F 3 "~" V 2450 1650 50  0001 C CNN
	1    2450 1550
	0    1    1    0   
$EndComp
$Comp
L Device:Speaker_Crystal LS1
U 1 1 6208F16A
P 3100 1350
F 0 "LS1" V 3112 1070 50  0000 R CNN
F 1 "Speaker_Crystal" V 3021 1070 50  0000 R CNN
F 2 "" H 3065 1300 50  0001 C CNN
F 3 "~" H 3065 1300 50  0001 C CNN
	1    3100 1350
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R?
U 1 1 620994D0
P 3850 1900
F 0 "R?" H 3920 1946 50  0000 L CNN
F 1 "R" H 3920 1855 50  0000 L CNN
F 2 "" V 3780 1900 50  0001 C CNN
F 3 "~" H 3850 1900 50  0001 C CNN
	1    3850 1900
	1    0    0    -1  
$EndComp
$Comp
L Device:Thermistor_NTC TH?
U 1 1 62099EA6
P 3850 2450
F 0 "TH?" H 3948 2496 50  0000 L CNN
F 1 "Thermistor_NTC" H 3948 2405 50  0000 L CNN
F 2 "" H 3850 2500 50  0001 C CNN
F 3 "~" H 3850 2500 50  0001 C CNN
	1    3850 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	3850 2050 3850 2150
Text Label 3500 1200 0    50   ~ 0
1=W1,2=Vcc
Text Label 1800 1300 0    50   ~ 0
1=CH2,2=GND
Text GLabel 4250 2150 2    50   Input ~ 0
CH1
Wire Wire Line
	4250 2150 3850 2150
Connection ~ 3850 2150
Wire Wire Line
	3850 2150 3850 2300
Wire Wire Line
	3200 1550 3200 1750
Wire Wire Line
	3200 1750 3850 1750
Wire Wire Line
	2650 1550 2650 2800
Wire Wire Line
	2650 2800 3300 2800
Wire Wire Line
	3850 2800 3850 2600
$Comp
L power:GND #PWR?
U 1 1 620A165C
P 3300 2850
F 0 "#PWR?" H 3300 2600 50  0001 C CNN
F 1 "GND" H 3305 2677 50  0000 C CNN
F 2 "" H 3300 2850 50  0001 C CNN
F 3 "" H 3300 2850 50  0001 C CNN
	1    3300 2850
	1    0    0    -1  
$EndComp
Wire Wire Line
	3300 2800 3300 2850
Connection ~ 3300 2800
Wire Wire Line
	3300 2800 3850 2800
Text GLabel 2050 1550 0    50   Input ~ 0
CH2
Wire Wire Line
	2050 1550 2250 1550
Text GLabel 3300 2150 2    50   Input ~ 0
W1
Wire Wire Line
	3100 1550 3100 2150
Wire Wire Line
	3100 2150 3300 2150
$EndSCHEMATC
