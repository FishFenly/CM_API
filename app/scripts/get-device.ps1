# session details
$cn = $args[0]
$server = "ngsccm-mp-01.northgatevehiclehire.net"
$sesh = New-PSSession -ComputerName $server -ConfigurationName Microsoft.PowerShell32 `
    -credential (Get-Credential)

Invoke-Command -Session $sesh -ScriptBlock {
    # Import the Cm module and cd into the psdrive
    Import-module "$($ENV:SMS_ADMIN_UI_PATH)\..\ConfigurationManager.psd1"
    cd "NUK:\"
    # get the device based on the first argument passed to invoke-cmd
    $out = Get-CMDevice | ? Name -like $args[0]
    # if $out is not null, get the mac adress and then convert it all into
    # json. Then return it. If it is null, return the str fail
    if ($out) {
        $mac = get-ciminstance -ClassName SMS_R_SYSTEM -Namespace root\sms\site_NUK |
            ? Name -like $($obj).Name | select -expand MacAddresses
        $x = @{
            name = ($out).Name
            mac = $mac
        } | convertto-json
        return $x
    } else { return 'fail' }
} -ArgumentList $cn