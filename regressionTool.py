import requests
import time
import json
from commandsByIntent import commandsList

# Instructions: replace your "from X import commandsList" with the correct list of commands you want to send from the commandsByIntent.py file

start_time=time.time()
# Insert deviceId and fakeAccountId value of device you are testing
deviceId = 1234567890
fakeAccountId = 999888777666
# Builds the cURL with the endpoint/url, satToken, and other needed parameters for the request
def speak_command(command):
    url = "http://fakeProductionOrLowerEnvEndpoint:1234/fakeAppId=STB&fakeFiltersAndOtherCurlParameters&Language=eng&deviceId={}&fakeAccountId={}&partnerid=fakePartner".format(deviceId, fakeAccountId)
         
    # "Authorization" parameter below must be updated with a newly generated SAT token every 24 hours
    # Other aspects of the cURL you are sending can be modified below e.g. key value pair for the cURL header
    headers = {
        'Content-Type': "text/plain",
        'Authorization': "Bearer <satToken>"
        }
    data = command
    response = requests.request("POST", url, headers=headers, data=data)
    print(response.json())
    return response

# This loop below  pulls the list of commands named commandsList within the file CommandsByIntent.py and works its way down from the top of the list of commands to the bottom.
# Once it gets to the last command in the list the program will stop. you can modify this list to replace it with any command you'd like to send.
# This is how you build group of commands for test cases in your test coverage (e.g. smoke, sanity, regression, top 100, etc.).
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
