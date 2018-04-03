import json
import urllib2
import uuid

class SmartPlug:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None

        self.tp_uuid = str(uuid.uuid4())

        self.login_req = {
         "method": "login",
         "params": {
         "appType": "Kasa_Android",
         "cloudUserName": self.username,
         "cloudPassword": self.password,
         "terminalUUID": self.tp_uuid
         }
        }

    def GetToken(self):
        try:
            req = urllib2.Request('https://wap.tplinkcloud.com')
            req.add_header('Content-Type', 'application/json')

            response = urllib2.urlopen(req, json.dumps(self.login_req))

            txt = response.read()
            jobj = json.loads(txt)
            self.token = jobj["result"]["token"]
        except:
            return

    def PrintDevices(self):
        try:
            if self.token is None:
                self.GetToken()

            getDeviceList_req = {"method": "getDeviceList" }

            url = 'https://wap.tplinkcloud.com?token=' + self.token
            req = urllib2.Request(url)
            req.add_header('Content-Type', 'application/json')

            response = urllib2.urlopen(req, json.dumps(getDeviceList_req))
            print response.read()
        except:
            return

    def GetState(self, device_id):
        try:
            if self.token is None:
                self.GetToken()

            status_req =  {"method":"passthrough", "params": {"deviceId": device_id, "requestData": "{\"system\":{\"get_sysinfo\":{}}}" }}

            url = 'https://wap.tplinkcloud.com?token=' + self.token
            req = urllib2.Request(url)
            req.add_header('Content-Type', 'application/json')

            response = urllib2.urlopen(req, json.dumps(status_req))
            txt = response.read()
            jobj = json.loads(txt)
            txt2 = jobj["result"]["responseData"]
            jobj2 = json.loads(txt2)
            return jobj2["system"]["get_sysinfo"]["relay_state"]
        except:
            return 0

    def TurnOn(self, device_id):
        try:
            if self.token is None:
                self.GetToken()

            turnOn_req = {"method":"passthrough", "params": {"deviceId": device_id, "requestData": "{\"system\":{\"set_relay_state\":{\"state\":1}}}" }}

            url = 'https://wap.tplinkcloud.com?token=' + self.token
            req = urllib2.Request(url)
            req.add_header('Content-Type', 'application/json')

            response = urllib2.urlopen(req, json.dumps(turnOn_req))
        except:
            return


    def TurnOff(self, device_id):
        try:
            if self.token is None:
                self.GetToken()

            turnOff_req = {"method":"passthrough", "params": {"deviceId": device_id, "requestData": "{\"system\":{\"set_relay_state\":{\"state\":0}}}" }}

            url = 'https://wap.tplinkcloud.com?token=' + self.token
            req = urllib2.Request(url)
            req.add_header('Content-Type', 'application/json')

            response = urllib2.urlopen(req, json.dumps(turnOff_req))
        except:
            return