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


Turn a Smart Plug On/Off

```
import TPLink

sp = TPLink.SmartPlug("username", "password")

state = sp.GetState("your_device_id")

if (state == 0):
    sp.TurnOn(MyDeviceID)
else:
    sp.TurnOff(MyDeviceID)
```
