# calibre-server
This script starts a Calibre server on startup and outputs server name and
 IP address to an LCD.  A momentary push-button is used to create a 
reboot or shutdown of the system.

To make this script bootable at startup:

```
mkdir /home/pi/.config/autostart
nano /home/pi/.config/autostart/calibre.desktop
```

```
[Desktop Entry]
Type=Application
Name=Calibre
Exec=/usr/bin/python3 /home/pi/calibre-server/calibre-boot.py
```

Reboot the Pi

### Task List
- [x] Make script start at bootup
- [x] Shutdown / reboot button
- [x] External LED power indicator
- [ ] Power switch
- [ ] Upload 3D printed bracket files
- [ ] Upload Eagle/KiCAD schematic
- [ ] Periodically query the server and parse response to make sure the server is still running
