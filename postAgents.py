import json
import requests

baseURL = 'http://localhost:8089'
user='admin'
password='admin'

auth = requests.post(baseURL + '/users/'+user+'/login?password='+password).json()
session = auth["session"]
headers = {'X-ArchivesSpace-Session':session, 'Content_Type':'application/json'}

agents = json.load(open('thecaptains.json'))
for i in range (0, len (agents)):
    agent = json.dumps(agents[i])
    post = requests.post(baseURL + '/agents/people', headers=headers, data=agent).json()
    print post
