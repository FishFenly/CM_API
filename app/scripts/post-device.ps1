# session details
$cn = $args[0]
$mac = $args[1]
$server = "ngsccm-mp-01.northgatevehiclehire.net"

$pw = cat .\scripts\securestring.txt | ConvertTo-SecureString
$cred = New-Object System.Management.Automation.PSCredential(
    "", $pw)

$sesh = New-PSSession -ComputerName $server -ConfigurationName Microsoft.PowerShell32 `
    -Credential ($cred)

Invoke-Command -Session $sesh -ScriptBlock {
    # Import the Cm module and cd into the psdrive
    Import-module "$($ENV:SMS_ADMIN_UI_PATH)\..\ConfigurationManager.psd1"
    cd "NUK:\"
    #  Create post function
    
} -ArgumentList $cn, $mac