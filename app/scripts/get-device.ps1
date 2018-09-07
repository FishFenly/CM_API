$cn = $args[0]
$server = "ngsccm-mp-01.northgatevehiclehire.net"
$sess = New-PSSession -ComputerName $server -ConfigurationName Microsoft.PowerShell32

Invoke-Command -Session $sess -ScriptBlock {
    Import-module "$($ENV:SMS_ADMIN_UI_PATH)\..\ConfigurationManager.psd1"
    cd "NUK:\"
    $out = Get-CMDevice | ? Name -like $args[0]
    if ($out) {
        $mac = gwmi -Class SMS_R_SYSTEM -Namespace root\sms\site_NUK |
            ? Name -like $($out).Name | select -expand MacAddresses
        $x = @{
            name = ($out).Name
            mac = $mac
        } | convertto-json
        return $x
    }
} -ArgumentList $cn