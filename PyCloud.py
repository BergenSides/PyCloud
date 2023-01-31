import os, json, websocket, requests

def SendPacket(Packet):
  Websocket.send(f"{json.dumps(Packet)}\n")

def SetupConnection(Username, ProjectID, Cookie):
  global User
  global ID
  global Websocket
  User = Username
  ID = str(ProjectID)
  Websocket = websocket.WebSocket()
  Websocket.connect(
    "wss://clouddata.scratch.mit.edu",
    cookie=f"scratchsessionsid={Cookie};",
    origin="https://scratch.mit.edu",
    enable_multithread=True
  )
  SendPacket({
    "method": "handshake",
    "user": Username,
    "project_id": str(ProjectID)
  })

def SetCloudVar(CloudName, Value):
  SendPacket({
  "method": "set",
  "name": f"☁ {CloudName}",
  "value": str(Value),
  "user": User,
  "project_id": ID,
  })

def GetCloudVar(CloudName):
  Limit = 100
  while True:
    Response = requests.get(f"https://clouddata.scratch.mit.edu/logs?projectid={ID}&limit={Limit}&offset=0").json()
    for x in range(100):
      if Response[x + Limit - 100]["name"] == f"☁ {CloudName}":
        return Response[x + Limit - 100]["value"]
    Limit += 100
