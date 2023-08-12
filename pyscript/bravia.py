import datetime
import requests
import json
import os 

try:
    from dotenv import load_dotenv
    load_dotenv()
    URL = f"http://{os.getenv('URL')}/sony/"
    headers = {"X-Auth-PSK": os.getenv('PASSWORD'), "Content-Type": "application/xml"}
except:
    print(f'Opps, couldnt find environment vars, please validate via "printenv"')
    raise

def tv_power_on():
    payload = '{\n    "method": "setPowerStatus",\n    "id": 55,\n    "params": [{"status": true\n    }],\n    "version": "1.0"\n}'
    response = requests.request("POST", URL + "system", headers=headers, data=payload)
    return response.text


def tv_power_off():
    payload = '{\n    "method": "setPowerStatus",\n    "id": 55,\n    "params": [{"status": false\n    }],\n    "version": "1.0"\n}'
    response = requests.request("POST", URL + "system", headers=headers, data=payload)
    return response.text


def tv_volume_up():
    payload = json.dumps(
        {
            "method": "setAudioVolume",
            "id": 98,
            "params": [{"volume": "+1", "ui": "on", "target": "speaker"}],
            "version": "1.2",
        }
    )
    response = requests.request("POST", URL + "audio", headers=headers, data=payload)
    return response.text


def tv_volume_down():
    payload = {
        "method": "setAudioVolume",
        "id": 98,
        "params": [{"volume": "-1", "ui": "on", "target": "speaker"}],
        "version": "1.2",
    }
    response = requests.request(
        "POST", URL + "audio", headers=headers, data=json.dumps(payload)
    )
    return response.text


def tv_volume_quiet():
    payload = {
        "method": "setAudioVolume",
        "id": 98,
        "params": [{"volume": "4", "ui": "on", "target": "speaker"}],
        "version": "1.2",
    }
    response = requests.request(
        "POST", URL + "audio", headers=headers, data=json.dumps(payload)
    )
    return response.text


def switch_to_hdmi():
    payload = {
        "method": "setPlayContent",
        "id": 101,
        "params": [{"uri": "extInput:hdmi?port=4"}],
        "version": "1.0",
    }
    response = requests.request(
        "POST", URL + "avContent", headers=headers, data=json.dumps(payload)
    )
    return response.text


def enter():
    payload = '<s:Envelope\n    xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"\n    s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">\n    <s:Body>\n        <u:X_SendIRCC xmlns:u="urn:schemas-sony-com:service:IRCC:1">\n            <IRCCCode>AAAAAQAAAAEAAABlAw==</IRCCCode>\n        </u:X_SendIRCC>\n    </s:Body>\n</s:Envelope>'
    headers = {
        "SOAPACTION": '"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC"',
        "X-Auth-PSK": "1234",
        "Content-Type": "text/xml; charset=UTF-8",
    }

    response = requests.request("POST", URL + "ircc", headers=headers, data=payload)

    return response.text
