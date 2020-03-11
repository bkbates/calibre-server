'''
	About:  This script is used for running a headless Calibre server.
			Additional functionality is included to display information
			when mounted in a server rack.
	
	Author: Brian Bates

	Date		Revision
	----		--------
	3/10/2020	Shutdown/reboot button added
	3/9/2020	Initial code with the LCD
	
	
	Tasks To-Do
	-----------
	- Shutdown / reboot button
	- Auto-start Calibre and server on boot
	- Auto-start this script on boot

'''
import RPi.GPIO as GPIO
from RPLCD import CharLCD
import subprocess
import time
import os

# Hide warnings from GPIO
GPIO.setwarnings(False)

# Initialize the LCD
lcd = CharLCD(cols=16, rows=2, numbering_mode=GPIO.BOARD, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

# Clear the screen
lcd.clear()
time.sleep(1)

# Write the Server Name
lcd.cursor_pos = (0, 0)
lcd.write_string("Server: Calibre")
time.sleep(2)

# Write the ip address
lcd.cursor_pos = (1, 0)
lcd.write_string(str(subprocess.check_output("hostname -I", shell=True))[2:17])

