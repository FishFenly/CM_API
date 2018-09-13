$sitecode = "NUK"
Import-module "$($ENV:SMS_ADMIN_UI_PATH)\..\ConfigurationManager.psd1"
cd "$($sitecode):\"
# get the first 20 devices of workstation type as an example output
$out = Get-CMDevice | select -First 20 | 
    ? DeviceOS -like "Microsoft Windows NT Workstation*"
# initalise the hash table
$x = @{}
# if getting the devices doesnt fail, loop through each device, get the mac and
# add it the hashtable we initialised. return the hashtable after converting it to
# JSON
if ($out) {
    foreach ($obj in $out) {
        $mac = get-ciminstance -ClassName SMS_R_SYSTEM -Namespace root\sms\site_NUK |
                    ? Name -like $($obj).Name | select -expand MacAddresses
        $x.add($obj.Name, $mac)
    }
    return ($x | convertto-json | % { [System.Text.RegularExpressions.Regex]::Unescape($_) })
} else { return 'fail' }