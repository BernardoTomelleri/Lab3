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
P 2450 1400
F 0 "MK1" V 2183 1400 50  0000 C CNN
F 1 "Microphone_Ultrasound" V 2274 1400 50  0000 C CNN
F 2 "" V 2500 1330 50  0001 L CNN
F 3 "~" V 2450 1500 50  0001 C CNN
	1    2450 1400
	0    1    1    0   
$EndComp
$Comp
L Device:R R1
U 1 1 620994D0
P 3850 1900
F 0 "R1" H 3920 1946 50  0000 L CNN
F 1 "10k" H 3920 1855 50  0000 L CNN
F 2 "" V 3780 1900 50  0001 C CNN
F 3 "~" H 3850 1900 50  0001 C CNN
	1    3850 1900
	1    0    0    -1  
$EndComp
$Comp
L Device:Thermistor_NTC TH1
U 1 1 62099EA6
P 3850 2450
F 0 "TH1" H 3948 2496 50  0000 L CNN
F 1 "Thermistor_NTC_10k@25C" H 3948 2405 50  0000 L CNN
F 2 "" H 3850 2500 50  0001 C CNN
F 3 "~" H 3850 2500 50  0001 C CNN
	1    3850 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	3850 2050 3850 2150
Text Label 3500 1200 0    50   ~ 0
1=W1,2=Vcc
Text Label 1800 1150 0    50   ~ 0
1=CH2,2=GND
Text GLabel 4250 2150 2    50   Output ~ 0
CH1
Wire Wire Line
	4250 2150 3850 2150
Connection ~ 3850 2150
Wire Wire Line
	3850 2150 3850 2300
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
$Comp
L Device:Speaker_Ultrasound LS1
U 1 1 620E3EA8
P 3250 1450
F 0 "LS1" V 3262 1170 50  0000 R CNN
F 1 "Speaker_Ultrasound" V 3171 1170 50  0000 R CNN
F 2 "" H 3215 1400 50  0001 C CNN
F 3 "~" H 3215 1400 50  0001 C CNN
	1    3250 1450
	0    -1   -1   0   
$EndComp
$EndSCHEMATC
