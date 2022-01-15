# example of voice commands that will be tested using my regressionTool, it will go from the top of the list and work it's way down to the bottom. commands can be changed on the fly or customized to group similar intents of commands (e.g. thermostat commands, light commands, arm/disarm commands, etc.). in a real world environment i have multiple files like this that are already grouped by their intents, top x amount of commands used in production by our users, regression test, sanity test, smoke test, etc. so i just need to update in the regressionTool which of the files to point to before running the program. 

commandsList = [
    "turn my lights on",
    "turn up bedroom thermostat heat",
    "is my system armed",
    "show front door camera"
    "turn my lights green"
]