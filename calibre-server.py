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
from gpiozero import Button
from RPLCD import CharLCD
import subprocess
import time
import os

# Hide warnings from GPIO
GPIO.setwarnings(False)


# Initialize the LCD
lcd = CharLCD(cols=16, rows=2, numbering_mode=GPIO.BCM, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11])

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

def shutdown():
	'''Shuts down the raspberry pi (actually, just a deep sleep)'''
	
	# Clear the screen
	lcd.clear()
	time.sleep(1)
	
	# Sleep for 3 more seconds to make sure the command is to shutdown
	# rather than reboot.  If the button is still held after 3 more
	# seconds, shutdown, otherwise, reboot.
	time.sleep(3)
	if button.is_held:
		# Notify user of shutdown
		lcd.cursor_pos = (0, 0)
		lcd.write_string("Shutting down")
		for i in range(3):
			time.sleep(1)
			lcd.cursor_pos = (0, i+13)
			lcd.write_string(".")
		
		time.sleep(1)
		lcd.clear()	
		os.system("sudo shutdown -h now")
	else:
		# Notify user of reboot
		lcd.cursor_pos = (0, 0)
		lcd.write_string("Rebooting")
		for i in range(3):
			time.sleep(1)
			lcd.cursor_pos = (0, i+9)
			lcd.write_string(".")
		
		time.sleep(1)
		lcd.clear()	
		os.system("sudo shutdown -r now")


# Shutdown / reboot button
button = Button(21)
button.when_held = shutdown

while(1):
	time.sleep(1)
