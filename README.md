# TPLink-SmartPlug
Python Class for controlling the Kasa TP-Link Smart Plug


## Usage:

Get Device ID:

```
import TPLink

sp = TPLink.SmartPlug("username", "password")

sp.PrintDevices()
```

Get the device id from the json parameter "deviceId"


Turn On/Off

```
import TPLink

sp = TPLink.SmartPlug("username", "password")

MyDeviceID = "your_device_id"

state = sp.GetState(MyDeviceID)

if (state == 0):
    sp.TurnOn(MyDeviceID)
else:
    sp.TurnOff(MyDeviceID)
```
