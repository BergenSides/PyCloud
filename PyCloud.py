import os, json, websocket, requests
ID = ""

def SendPacket(Packet):
  Websocket.send(f"{json.dumps(Packet)}\n")

def SetupConnection(Username, ProjectID, Cookie):
  global User
  global ID
  global Websocket
  User = Username
  if str(type(ProjectID)) == "<class 'dict'>":
    ID = []
    for x in range(len(ProjectID)):
      ID.append(ProjectID[x])
  else:
    ID = str(ProjectID)
  Websocket = websocket.WebSocket()
  Websocket.connect(
    "wss://clouddata.scratch.mit.edu",
    cookie=f"scratchsessionsid={Cookie};",
    origin="https://scratch.mit.edu",
    enable_multithread=True
  )
  if str(type(ProjectID)) == "<class 'dict'>":
    for x in range(len(ID)):
      SendPacket({
        "method": "handshake",
        "user": Username,
        "project_id": ID[x]
      })
  else:
    SendPacket({
      "method": "handshake",
      "user": Username,
      "project_id": ID
    })
  
def SetCloudVar(CloudName, Value, ProjectID=""):
  if ProjectID == "":
    ProjectID = ID
  SendPacket({
  "method": "set",
  "name": f"☁ {CloudName}",
  "value": str(Value),
  "user": User,
  "project_id": ProjectID,
  })

def GetCloudVar(CloudName, ProjectID=""):
  Limit = 100
  if ProjectID == "":
    ProjectID = ID
  while True:
    Response = requests.get(f"https://clouddata.scratch.mit.edu/logs?projectid={ProjectID}&limit={Limit}&offset=0").json()
    for x in range(100):
      if Response[x + Limit - 100]["name"] == f"☁ {CloudName}":
        return Response[x + Limit - 100]["value"]
    Limit += 100
