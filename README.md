# WindowsLockerRFID
A simple python script to lock your Windows session when an RFID card (of your choice) is removed from the reader connected to the computer.

### Build .exe from .py
To create your executable usable on Windows, I recommend to use PyInstaller with the -F argument to create a single file, as well as the -w option to avoid displaying a command prompt that will be permanent since we are in an infinite While loop.

Build executable : 
```
pyinstaller -F -w /path/to/file/lockwin.py
```

### Create a installer
To create an installer I usually use inno Setup, which is a simple Pascal script and will allow me to add a lot of options.
In our case it is useful to not allow the user to change the installation directory, because it is hard written in the code.

### Home Assistant Integration
You can also integrate the reader status and the profile of the read RFID card to send it to Home Assistant, it will be based on the CardPresentLog.txt and ProfileCardLog.txt files located in the installation directory.

Use the Hass agent and a sensor retrieving data in Powershell, then add this line: 
```
Get-Content "C:\Users\%USERNAME%AppData\LocalPrograms\WinLockerRFID\CardPresentLog.txt"
```
