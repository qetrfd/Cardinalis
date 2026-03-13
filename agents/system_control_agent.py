import os
import subprocess

def volume_up():
    os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'")

def volume_down():
    os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 10)'")

def wifi_on():
    subprocess.run(["networksetup","-setairportpower","airport","on"])

def wifi_off():
    subprocess.run(["networksetup","-setairportpower","airport","off"])