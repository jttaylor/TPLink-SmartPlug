import TPLink

##token = TPLink.GetToken()
##print token

sp = TPLink.SmartPlug("username", "password")

MyDeviceID = "your_device_id"
sp.PrintDevices()
#sp.TurnOff()
state = sp.GetState(MyDeviceID)

if (state == 0):
    sp.TurnOn(MyDeviceID)
else:
    sp.TurnOff(MyDeviceID)
