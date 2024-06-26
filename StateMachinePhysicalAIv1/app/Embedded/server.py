from flask import Flask, request, jsonify
import pathlib
import json
import time
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
    player = move_data['player'] # player number (0 - 3)
    deltaPos = move_data['deltaPos'] # change (dice roll) in player position (1 - 12)
    currPos = move_data['currPos']  # current player position - after delta position is applied (1 - 40)
    print("[MOTOR] Current Motor Position: ", motorPos) # line for debugging
    if player == -1:
        rotation = 5*motorPos
        print("[MOTOR] Reset Rotation: ", rotation) # line for debugging
        turnMotor(rotation, True)
        return
    # Move the motor to the initial pos of the player
    rotation = 5*(currPos - deltaPos - motorPos)
    if rotation >= 200: rotation %= 40
    elif rotation <= -200: rotation %= -40
    print("[MOTOR] Pick-up Rotation: ", rotation) # line for debugging
    # going to the piece (currPos - deltaPos)
    if rotation > 0:
        turnMotor(rotation, False)
    else:
        turnMotor(-rotation, True)
    moveRot = 5*deltaPos
    print("[MOTOR] Move Rotation: ", moveRot) # line for debugging
    electromagnetOn(player)
    time.sleep(0.5)
    # Move player here. going to currPos
    if deltaPos > 0:
        turnMotor(moveRot, False)
    else:
        turnMotor(-moveRot, True)
    motorPos = currPos
    print("[MOTOR] Final Motor Position: ", motorPos) # line for debugging
    electromagnetOff(player)
    time.sleep(0.5)

# Move motor route
@app.route('/move', methods=['POST'])
def move_one():
    received = request.get_json()
    process_json(received)
    res = jsonify({})
    res.status_code = 201 # Status code for "created"
    return res

if __name__ == '__main__':
    app.run(host='172.20.10.4', port=4444)