#Author: Sharad Talekar
#Date: 03Feb2015
#Purpose: File IO operations
import os


fh = open("vstorm.txt","w")
fh.write("----------------------2015 Suzuki V-Storm 650 ABS Adventure Specs----------------------------------\n")
fh.write("****************************************************************************************************\n\n\n")
fh.write("Engine: \n645 cc, 4-stroke, 2-cylinder, liquid-cooled, DOHC, 90-degree V-Twin\n")
fh.write("Bore x Stroke - 81.0 mm x 62.6 mm (3.189 in x 2.465 in), Compression Ratio - 11.2 : 1 ,Fuel System - Suzuki Fuel Injection, Electric Start, Lube - Wet sump\n")
fh.write("CHASSIS:\nSuspension Front - Telescopic, coil spring, oil damped\nSuspension Rear - Link type, coil spring, oil damped\nBrakes Front - Disc, twin\nBrakes Rear - Disc\nTires Front - 110/80R19M/C 59H, tubeless\nTires Rear -	150/70R17M/C 69H, tubeless\nFuel Tank Capacity - 5.3 US\n")
fh.write("Color: \nPearl Bracing White, Metallic Triton Blue\n")
fh.write("ELECTRICAL:\nIgnition	- Electronic ignition (Transistorized)\n")
fh.write("DIMENSIONS AND CURB WEIGHT:\nOverall Length - 2290 mm (90.2 in), Overall Width - 835 mm (32.9 in)\nWheelbase - 1560 mm (61.4 in)\nGround Clearance - 175 mm (6.9 in)\nSeat Height - 835 mm (32.9 in)\nCurb Weight - 214 kg (472 lbs)\n")
fh.write("WARRANTY: \n12 month unlimited mileage limited warranty.\n")
print "file saved at location: ", 
os.system('chdir')

fh.close()

#fh = open("vstorm.txt","a")

#fh.close()
