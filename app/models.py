class Devices(cn):
    """ Devices class, post and get devices using name """
    def __init__(self, cn):
        self = cn

    def post(self):
        """ Post a device to the configmgr DB """
        p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy',
                            'bypass', 'scripts\\post-device.ps1', cn], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.communicate()

        return output

    def get(self):
        """ Get device from configmgr and return whether it exists or not """
        p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy',
                            'bypass', 'scripts\\get-device.ps1', cn], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.communicate()

        return output