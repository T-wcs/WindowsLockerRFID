# 🖥🔐 WindowsLockerRFID
This is a basic program that automatically locks the session if the NFC/RFID card is not present on the USB badge reader connected to the Windows computer.

- - -

### ⚠️ Requirements
It is necessary to have the pyscard library installed : https://github.com/LudovicRousseau/pyscard
and the paho-mqtt client library if you want to send your data via mQTT : https://github.com/eclipse/paho.mqtt.python

You can simply run the following command to install the packages:

```bash
pip install -r requirements.txt
```

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

### 📑 Parsing output data with Hass Agent on Windows.

To create a sensor with the result data from `output.json` you need create a PowerShell sensor on Hass Agent.
In the script or command section of the Hass agent PowerShell sensor, add the following lines depending on the data you want to obtain :  

![image](https://user-images.githubusercontent.com/70718793/216603072-37a763d3-cfc9-4389-a621-f0902fe2cbc9.png)


To retrieve the Card UID
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.CardUID
```

To retrieve the Card profile : 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.ProfileCard
```

To retrieve the Reader status : 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.Status
```

To retrieve the Windows Version : 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.WindowsVersion
```

To retrieve the HostName : 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.HostName
```

To retrieve the Reader Name : 
```
$json = Get-Content "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json" | ConvertFrom-Json; $json.WinlockerDetails.ReaderName
```  
Output :  
![image](https://user-images.githubusercontent.com/70718793/216600295-802695cd-eb30-4447-9cff-cccffa7204e1.png)

- - -
  
### 📡 MQTT module
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
In your Home Assistant `configuration.yaml` file it will also be necessary to add the following lines: 

```yaml
mqtt:        
  sensor:
    - name: "Winlocker Status"
      state_topic: "homeassistant/sensor/WinLockerRFID/config"
      value_template: "{{ value_json.WinlockerDetails.Status }}"
      json_attributes_topic: "homeassistant/sensor/WinLockerRFID/attributes"

    - name: "Winlocker Card UID"
      state_topic: "homeassistant/sensor/WinLockerRFID/config"
      value_template: "{{ value_json.WinlockerDetails.CardUID }}"
      json_attributes_topic: "homeassistant/sensor/WinLockerRFID/attributes"
      
    - name: "Winlocker Profile Card"
      state_topic: "homeassistant/sensor/WinLockerRFID/config"
      value_template: "{{ value_json.WinlockerDetails.CardProfile }}"
      json_attributes_topic: "homeassistant/sensor/WinLockerRFID/attributes"     
```

Now you can search for the entity with the name given to the variable `name` in the `configuration.yaml` file

Example with `Winlocker Status` into `Development Tools > State`

![image](https://user-images.githubusercontent.com/70718793/216605130-d5cd55e4-58b1-4528-ab53-52451132c67e.png)

- - -

## ✅ Reader tested

ACR122U : 

![image](https://user-images.githubusercontent.com/70718793/216606983-4b173acc-3de6-4d36-b745-740682d86ed6.png)

- - -

WCR 330 :  

![image](https://user-images.githubusercontent.com/70718793/216606870-abc95a26-724e-4f33-87b2-4bac23b708d1.png)

- - -

### Improvement
1. Create a table to manage the different readers (ACR122U / WCR330 etc)
