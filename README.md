# PyCloud
Welcome to PyCloud, my horrible attempt at making a module that connects to scratch.

As of right now, there is no way to import or otherwise install PyCloud, I will upload it to PyPi in coming time, once I have the time.<br /><br /><br /><br />



To begin using PyCloud, start by initializing a connection using:<br />
`SetupConnection(Username, ProjectID, SessionID)`

After this, you can set a cloud variable using:<br />
`SetCloudVar(CloudVariableName, Value)`

Or you can get a cloud variable's value using:<br />
`GetCloudVar(CloudVariableName)`



ADVANCED USAGE:

To connect multiple projects:<br />
`Projects = [Project1, Project2...]<br />
SetupConnection(Username, Projects, SessionID)`

To change variables do this:<br />
`SetCloudVar(CloudVariableName, Value, Projects[NumberOfProjectInList])`

To get a variable do this:<br />
`GetCloudVar(CloudVariableName, Projects[NumberOfProjectInList])`
