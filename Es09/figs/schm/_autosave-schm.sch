EESchema Schematic File Version 5
EELAYER 36 0
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
Comment5 ""
Comment6 ""
Comment7 ""
Comment8 ""
Comment9 ""
$EndDescr
Connection ~ 3300 2800
Connection ~ 3850 1750
Connection ~ 3850 2250
Wire Wire Line
	2650 1750 2650 2800
Wire Wire Line
	2650 1750 3150 1750
Wire Wire Line
	2650 2800 3300 2800
Wire Wire Line
	2800 1950 2800 2100
Wire Wire Line
	2800 2100 2900 2100
Wire Wire Line
	3250 1750 3250 1950
Wire Wire Line
	3250 1950 2800 1950
Wire Wire Line
	3300 2800 3300 2850
Wire Wire Line
	3300 2800 3850 2800
Wire Wire Line
	3350 1750 3350 2100
Wire Wire Line
	3350 2100 3500 2100
Wire Wire Line
	3450 1750 3850 1750
Wire Wire Line
	3850 1750 3850 1900
Wire Wire Line
	3850 1750 4250 1750
Wire Wire Line
	3850 2200 3850 2250
Wire Wire Line
	3850 2250 3850 2350
Wire Wire Line
	3850 2250 4250 2250
Wire Wire Line
	3850 2650 3850 2800
Text GLabel 2900 2100 2    50   Output ~ 0
CH2
Text GLabel 3500 2100 2    50   Input ~ 0
W1
Text GLabel 4250 1750 2    50   Input ~ 0
VCC
Text GLabel 4250 2250 2    50   Output ~ 0
CH1
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
$Comp
L Device:R R1
U 1 1 620994D0
P 3850 2050
F 0 "R1" H 3920 2096 50  0000 L CNN
F 1 "10k" H 3920 2005 50  0000 L CNN
F 2 "" V 3780 2050 50  0001 C CNN
F 3 "~" H 3850 2050 50  0001 C CNN
	1    3850 2050
	1    0    0    -1  
$EndComp
$Comp
L Device:Thermistor_NTC TH1
U 1 1 62099EA6
P 3850 2500
F 0 "TH1" H 3948 2546 50  0000 L CNN
F 1 "Thermistor_NTC_10k@25C" H 3948 2455 50  0000 L CNN
F 2 "" H 3850 2550 50  0001 C CNN
F 3 "~" H 3850 2550 50  0001 C CNN
	1    3850 2500
	1    0    0    -1  
$EndComp
$Comp
L Device:Microphone_Ultrasound MK1
U 1 1 62090EE7
P 3100 1050
F 0 "MK1" V 2833 1050 50  0000 C CNN
F 1 "Microphone_Ultrasound" V 2924 1050 50  0000 C CNN
F 2 "" V 3150 980 50  0001 L CNN
F 3 "~" V 3100 1150 50  0001 C CNN
	1    3100 1050
	0    1    1    0   
$EndComp
$Comp
L Device:Speaker_Ultrasound LS1
U 1 1 620E3EA8
P 3450 1000
F 0 "LS1" V 3462 720 50  0000 R CNN
F 1 "Speaker_Ultrasound" V 3371 720 50  0000 R CNN
F 2 "" H 3415 950 50  0001 C CNN
F 3 "~" H 3415 950 50  0001 C CNN
	1    3450 1000
	0    -1   -1   0   
$EndComp
$Comp
L New_Library:HC-SR04 U?
U 1 1 00000000
P 3300 1550
F 0 "U?" V 2900 2050 60  0000 L CNN
F 1 "HC-SR04" V 3050 2050 60  0000 L CNN
F 2 "" H 3300 1550 60  0000 C CNN
F 3 "" H 3300 1550 60  0000 C CNN
	1    3300 1550
	0    1    1    0   
$EndComp
$EndSCHEMATC
