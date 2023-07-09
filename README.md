# Sound-Quality-Monitoring-System-I2S-protocol
# ABSTRACT 
Sound intensity in the air is evaluated in this reasearch so that we can consider the quality of the sound in some specific area whether it is good or not via Decibel(dB) parameter. Many types of sounds we hear every single days in modern life through discussion, talking, vehicles, entertainments,... Not most of them are exactly what we expect to hear, aside from charming and valuable sound, there are aslo annoying ones which is all called noise in general and they seem profitless until now, they might cause bad effects on us – human being like bothersome noise come from the factory, loud sound from transporting vehicles when you are moving on the road or just living nearby and maybe it is from your household electrical appliances; their source appear arround our activities, poor urban planning may give rise to noise disintegration or pollution, side-by-side industial and residential buidings can result in noise pollution in residential areas. Raspberry Pi Zero W is a decent device for this project due to its Wifi connection comes with ICS43434 MEMS Breakout that support I2S - an indispendable part in our analysis there are also extra library code that we need to have sound magnitude measured such as pyaudio and spl_lib(sound pressure level), recorded signal is processed and then being uploaded to Firebase realtime database service. This result could be premiss for later advanced studies in the future.
# 1.	INTRODUCTION 
Nowadays, noise pollution is becoming more and more common, it directly affects humans and animals so it needs more research. Not all sound is considered noise pollution. The World Health Organization (WHO) defines noise above 65 decibels (dB) as noise pollution. To be precise, noise becomes harmful when it exceeds 75 decibels (dB) and is painful above 120 dB. Causes of  noise pollution, traffic noise, air traffic noise, construction sites, catering and night life, animal,…Effects of noise pollution, as well as damaging our hearing by causing – tinnitus or deafness, constant loud noise can damage human health in many ways, particularly in the very young and the very old, here are some of the  main ones:
Physical: Respiratory agitation, racing pulse, high blood pressure, headaches and, in case of extremely loud, constant noise, gastritis, colitis and even heart attacks.
Psychological: Noise can cause attacks of stress, fatigue, depression, anxiety and hysteria in both humans and animals.
Sleep and behavioural disorders: Noise above 45 dB stops you from falling asleep or sleeping properly. Remember that according to the World Health Organization it should be no more than 30 dB. Loud noise can have latent effects on our behaviour, causing aggressive behaviour and irritability.
Memory and concentration: Noise may affect people's ability to focus, which can lead to low performance over time. It is also bad for the memory, making it hard to study. Interestingly, our ears need more than 16 hours' rest to make up for two hours of exposure to 100 dB. 
SOLUTIONS TO REDUCE NOISE POLLUTION:
International bodies like the WHO agree that awareness of noise pollution is essential to beat this invisible enemy. For example: avoid very noisy leisure activities, opt for alternatives means of transport such as bicycles or electric vehicles over taking the car, do your housework at recommended times, insulate homes with noise-absorbing materials, etc. Educating the younger generation is also an essential aspect of environmental education.
Governments can also take measures to ensure correct noise management and reduce noise pollution. For example: protecting certain areas — parts of the countryside, areas of natural interest, city parks, etc. — from noise, establishing regulations that include preventive and corrective measures — mandatory separation between residential zones and sources of noise like airports, fines for exceeding noise limits, etc. —, installing noise insulation in new buildings, creating pedestrian areas where traffic is only allowed to enter to offload goods at certain times, replacing traditional asphalt with more efficient options that can reduce traffic noise by up to 3 dB, among others.
Sound quality monitoring is also one way to address and limit noise pollution. So this project is put into research
The goal of the project is to build a measuring and monitoring system for sound through the internet, as follows:
I2S (Inter-IC Sound), bypassing analog signal processing (ADC).
•	The system coverage over the sensor nodes (Node) and the central processor (Gateway) can be very far apart, coverage with a range of km2.
•	Data storage that can be retrieved on cloud database.
•	Observe the device location on the map The topic is also the prerequisite for developing projects related to audio signal processing because this is a very potential area for development.
I²S (Inter-IC Sound), pronounced eye-squared-ess, is an electrical serial bus interface standard used for connecting digital audio devices together. It is used to communicate PCM audio data between integrated circuits in an electronic device. The I²S bus separates clock and serial data signals, resulting in simpler receivers than those required for asynchronous communications systems that need to recover the clock from the data stream. Alternatively I²S is spelled I2S (pronounced eye-two-ess) or IIS (pronounced eye-eye-ess). Despite the similar name, I²S is unrelated to the bidirectional I²C (IIC) bus.
Advantages of the I2S standard: 
•	Using separate Clock and serial data line should have a simpler design than other asynchronous systems. 
•	Reliable data synchronization thanks to Master device.
•	The results obtained are of good quality, high stability. 
•	Output is purely digital due to the removal of ADC / DAC and preamplification components commonly found in legacy standards (as can be seen in firuge 1).

![image](https://github.com/KienNguyen9/Sound-Quality-Monitoring-System-I2S-protocol/assets/136218538/39a54f59-fbe8-4a0d-9860-1951661123f9)

Figure 1. Diffrence between I2S and ADC

# Hardware used in the project
Module MEMS Microphone ICS43434 
The ICS-43434 is digital I²S output bottom port microphone. The complete ICS-43434 solution consists of a MEMS sensor, signal conditioning, an analog-to-digital converter, decimation and antialiasing filters, power management, and an industry standard 24-bit I²S interface. The I²S interface allows the ICS-43434 to connect directly to digital processors, such as DSPs and microcontrollers, without the need for an audio codec in the system. The ICS-43434 has multiple modes of operation: High Performance, Low Power (AlwaysOn), Sleep. The ICS-43434 has high SNR and 120 dB SPL AOP in all operational modes. The ICS-43434 has a high SNR of 64 dBA and a wideband frequency response. The sensitivity tolerance of the ICS‐43434 is ±1 dB, which enables high performance microphone arrays without the need for system calibration. The ICS-43434 is available in a small 3.50 mm × 2.65 mm × 0.98 mm surface-mount package. The ICS-43434 is function-compatible with the ICS-43432 while providing equivalent electro-acoustic performance at lower power consumption and in a smaller package. 

![image](https://github.com/KienNguyen9/Sound-Quality-Monitoring-System-I2S-protocol/assets/136218538/baecf883-4b47-4215-bd25-8870fb1019a6)

Transmit RF signals 
In this project we use the LoRa Ra-02 module to transmit audio data from the sensor nodes to the gateway, because:
Advantages
•	Cheap price
•	Easy to buy 
Disadvantages 
•	Limited transmission distance 
•	susceptible to interference

![image](https://github.com/KienNguyen9/Sound-Quality-Monitoring-System-I2S-protocol/assets/136218538/4f11eb16-31b9-4d59-8286-2d00443ac780)

Raspberry Pi 3B and  Raspberry Pi zero
In this project we use: Raspberry Pi 3B embedded computer as gateway to capture data from sensor nodes and then upload to cloud database. At the sensor nodes we used a Raspberry Pi Zero embedded computer to capture audio data and GPS coordinates and send it to the gateway.
The Raspberry Pi 3B is powerful enough to be a Gateway and has support for both wifi and an enthernet gateway to reliably upload data to the cloud database. Also on the sensor button we chose raspberryPiZero because it is powerful, supports the I2S standard and is reasonably priced


![image](https://github.com/KienNguyen9/Sound-Quality-Monitoring-System-I2S-protocol/assets/136218538/6b3e5e00-aba0-4109-847d-8def4479b0cb)

![image](https://github.com/KienNguyen9/Sound-Quality-Monitoring-System-I2S-protocol/assets/136218538/f07f4dcf-2536-44c5-80dc-8740c5b8d4e9)

The module used for positioning is GPS U-Blox-7N with high accuracy and fast response time 

![image](https://github.com/KienNguyen9/Sound-Quality-Monitoring-System-I2S-protocol/assets/136218538/fb1eeb60-6e46-4331-8631-60e0290390f8)

 ![image](https://github.com/KienNguyen9/Sound-Quality-Monitoring-System-I2S-protocol/assets/136218538/66d9f019-f388-479b-842b-0bc44a6c30f2)

.









