# cron: run the script when boot

# pip install Flask
# pip install gpiozero

"""
define RelayBoard RB
define Motherboard MB

Connection RPI and Relay board
 GPIO17 -> RB IN1
 GPIO27 -> RB IN2
 5V     -> RB VCC
 GND    -> RB GND
 
Connection Relay board and motherboard
 RB NO1  -> MB PWR+
 RB COM1 -> MB PWR-
 RB NO2  -> MB RST+
 RB COM2 -> MB RST-
 
Split male PWR+ PWR- RST+ RST- to 2 female connectors,
so that they can be controlled by relays and regular buttons.
"""

from flask import Flask, request
from gpiozero import DigitalOutputDevice
from time import sleep



app = Flask(__name__)
secret = 'somesecret'

# pin numbering: use GPIOXX number instead of board pin number
relayBoot = DigitalOutputDevice(17, active_high=False, initial_value=False) # board pin number 11
relayReboot = DigitalOutputDevice(27, active_high=False, initial_value=False) # 13

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/boot')
def boot():
    inputSecret = request.args.get('secret')
    if inputSecret == secret:
        relayBoot.on()
        sleep(0.3)
        relayBoot.off()
        return "OK"
    else:
        return "secret not correct"

@app.route('/reboot')
def reboot():
    inputSecret = request.args.get('secret')
    if inputSecret == secret:
        relayReboot.on()
        sleep(0.3)
        relayReboot.off()
        return "OK"
    else:
        return "secret not correct"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
 
