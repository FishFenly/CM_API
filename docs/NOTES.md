# Language
Python - Occasionally using pwsh and WMI to interface with CM easier

# Functionality
An interface into SCCM to figure out if a device exists and is in an OSD collection. If it exists and doesnt appear in the right collection, then return that to the frontend and add to the build collection if required.
If not in the database, get the mac and device name from the device and import.

# Endpoints
* /osd/v1.0/devices
** GET devices from the CM db or POST devices - possibly will need to use powershell to interface with CM 
