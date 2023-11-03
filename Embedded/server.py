from flask import Flask, request, jsonify
import pathlib
import motor

# Define Flask server
app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file
motorPos = 0

# Function to process the json data received by the server
def process_json(move_data):
    # Parse the json for the title and artist using dictionary indexing
    player = move_data['player']
    deltaPos = move_data['deltaPos']
    currPos = move_data['currPos']
    # Move the motor to the initial pos of the player
    motor.turnMotor(currPos - motorPos)
    motorPos = currPos
    # Move player here
    motor.turnMotor(deltaPos)
    motorPos = motorPos + deltaPos

# Move motor route
@app.route('/move', methods=['POST'])
def move_one():
    received = request.get_json()
    process_json(received)
    res = jsonify({})
    res.status_code = 201 # Status code for "created"
    return res

if __name__ == '__main__':
    app.run(host='172.20.10.11', port=5000)