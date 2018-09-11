import subprocess
import os

dirname = os.path.join(os.path.dirname(__file__), 'scripts/')

def post(cn, mac):
    """ Post a device to the configmgr DB """
    p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy',
                        'bypass', dirname + 'post-device.ps1', cn, mac], 
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()

    return output

def getall():
    """ Get first 20 devices from configmgr and returns them """
    p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy',
                        'bypass', dirname + 'get-alldevices.ps1'], 
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()

    return output

def get(cn):
    """ Get device from configmgr and return whether it exists or not """
    p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy',
                        'bypass', dirname + 'get-device.ps1', cn], 
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()

    return output