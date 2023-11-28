from flask import Flask, request, jsonify
import pathlib
import json
from motor import *

# Define Flask server
app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file
motorPos = 0

# Function to process the json data received by the server
def process_json(move_data):
    global motorPos
    move_data = json.loads(move_data) # convert json string to json object dictionary
    # Parse the json for the title and artist using dictionary indexing
    player = move_data['player']
    deltaPos = move_data['deltaPos']
    currPos = move_data['currPos']
    print("This is data: ", move_data) # line for debugging
    # Move the motor to the initial pos of the player
    rotation = 5*(currPos - motorPos)
    print(rotation)
    if rotation > 0:
        turnMotor(rotation, True)
    else:
        turnMotor(-rotation, False)
    motorPos = currPos
    electromagnetOn(player)
    # Move player here
    if deltaPos > 0:
        turnMotor(rotation, True)
    else:
        turnMotor(-rotation, False)
    motorPos = motorPos + deltaPos
    electromagnetOff(player)

# Move motor route
@app.route('/move', methods=['POST'])
def move_one():
    received = request.get_json()
    print(received, ":::")
    print(type(received))
    process_json(received)
    res = jsonify({})
    res.status_code = 201 # Status code for "created"
    return res

if __name__ == '__main__':
    app.run(host='172.20.10.11', port=5000)