# WindowsLockerRFID
A simple python script to lock your Windows session when an RFID card (of your choice) is removed from the reader connected to the computer.

- - -

### 🔩 Build .exe from .py
To create your executable usable on Windows, I recommend to use PyInstaller with the -F argument to create a single file, as well as the -w option to avoid displaying a command prompt that will be permanent since we are in an infinite While loop.

Build executable : 
```
pyinstaller -F -w --hidden-import=modules.* /path/to/file/main.py -p "C:\Users\%USERNAME\Path_to_repository"
```

### ⚙️ Create a installer
To create an installer I usually use inno Setup, which is a simple Pascal script and will allow me to add a lot of options.
In our case it is useful to not allow the user to change the installation directory, because it is hard written in the code.

- - -

### 🏠 Home Assistant Integration
You can also integrate the reader status, UID and profile of the read RFID card to send it to Home Assistant, it will be based on the `output.json` file located in the installation directory.

Structure of `output.json` : 

```json
{
    "WinlockerDetails": {
        "Status": "Connected",
        "ConnectionType": "USB",
        "HostName": "DESKTOP-EXAMPLE",
        "WindowsVersion": "Windows-10-10.0.19044-SP0",
        "ReaderName": "WCR WCR330-ContactLess Reader 0",
        "CardUID": "01020304",
        "CardProfile": "JohnDoe"
    }
}
```

- - -

### Parsing output data with Hass Agent on Windows.

To create a sensor with the result data from output.json you need create a PowerShell sensor on Hass Agent.

Use the Hass agent and a sensor retrieving UID card in Powershell, then add this line: 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\LocalPrograms\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.CardUID
```

To retrieve the profile card in Powershell, then add this line: 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\LocalPrograms\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.ProfileCard
```

To retrieve the reader status in Powershell, then add this line: 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\LocalPrograms\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.Status
```

To retrieve the Windows Version in Powershell, then add this line: 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\LocalPrograms\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.WindowsVersion
```

To retrieve the HostName in Powershell, then add this line: 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\LocalPrograms\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.HostName
```

To retrieve the Reader Name in Powershell, then add this line: 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\LocalPrograms\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.ReaderName
```  
Output :  
![image](https://user-images.githubusercontent.com/70718793/216600295-802695cd-eb30-4447-9cff-cccffa7204e1.png)
  
### MQTT module
The code is now able to send data via the MQTT protocol based on a configuration file `mqttConfig.json` with the following structure:

```json
{
  "hostname":"homeassistant.lan",
  "Port": 1883,
  "login": "YOU_LOGIN",
  "password": "YOU_PASSWORD",
  "topic": "homeassistant/sensor/WinLockerRFID/config"
}
```  

It will automatically send the data found in the `output.json` file to the topic found in the configuration file.

- - -

### Improvement
1. Create a table to manage the different readers (ACR122U / WCR330 etc)
