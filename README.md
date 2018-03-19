# TPLink-SmartLink
Python Class for controlling the Kasa TP-Link Smart Plug


Usage:

import TPLink

sp = TPLink.SmartPlug("username", "password")

sp.PrintDevices()
MyDeviceID = "your_device_id"

state = sp.GetState(MyDeviceID)

if (state == 0):
    sp.TurnOn(MyDeviceID)
else:
    sp.TurnOff(MyDeviceID)
