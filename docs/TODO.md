# Todo
* fix the fact that the pwsh scripts return object types that the flask app cannot read
* post script
* the app will need to run on the cm server so invoke command wont work so need to change all the pwsh scripts to remove the invoke command stuff
* look into whether I can not use WMI, because querying WMI for the mac takes so long, maybe a SQL query would be better