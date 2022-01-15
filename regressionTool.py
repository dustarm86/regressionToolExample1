import requests
import time
import json
from commandsByIntent import commandsList

# instructions: replace your "from X import commandsList" with the correct list of commands you want to send

start_time=time.time()
# insert receiverId value of device you are testing
DeviceId = 1234567890

def speak_command(command):
    url = "http://fakeProductionOrLowerEnvEndpoint:1234/fakeAppId=STB&fakeFiltersAndOtherCurlParameters&Language=eng&DeviceId={}&partnerid=fakePartner".format(DeviceId)
         
     
#  "Authorization" parameter below must be updated with a newly generated SAT token every 24 hours
    headers = {
        'Content-Type': "text/plain",
        'Authorization': "Bearer <satToken>"
        }
    data = command
    response = requests.request("POST", url, headers=headers, data=data)

    #print(response.text)
    print(response.json())
    return response
    #json.load(response.text)

stuff_to_yell_at_remote = commandsList
for command in stuff_to_yell_at_remote:
    speak_command("exit")
    time.sleep(1)
    speak_command("exit")
    time.sleep(2)
    speak_command(command)
    time.sleep(15)
    speak_command("exit")
    time.sleep(1)

print("\nThe program took ", (time.time() - start_time) / 60, " minutes to run.")