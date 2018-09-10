import subprocess

class Devices():
    """ Devices class, post and get devices using name """
    def post(self, cn, mac):
        """ Post a device to the configmgr DB """
        p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy',
                            'bypass', 'scripts\\post-device.ps1', cn, mac], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.communicate()

        return output

    def getall(self):
        """ Get all device from configmgr and return """
        p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy',
                            'bypass', 'scripts\\get-device.ps1'], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.communicate()

        return output

    def get(self, cn):
        """ Get device from configmgr and return whether it exists or not """
        p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy',
                            'bypass', 'scripts\\get-device.ps1', cn], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.communicate()

        return output