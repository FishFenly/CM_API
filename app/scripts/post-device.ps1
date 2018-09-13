# session details
$cn = $args[0]
$mac = $args[1]
$btype = $args[2]

$id = 'NUK0001F'

# Import the Cm module and cd into the psdrive
Import-module "$($ENV:SMS_ADMIN_UI_PATH)\..\ConfigurationManager.psd1"
cd "NUK:\"
#  Create post function
if ($btype -eq 'new') {
	Import-CMComputerInformation -computername $cn -macaddress $mac -collectionid $id
} elseif ($btype -eq 'rebuild') {
	Add-CMDeviceCollectionDirectMembershipRule -collectionid $id
} else { return 'fail' }