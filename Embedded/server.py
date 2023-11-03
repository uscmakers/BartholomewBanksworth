from flask import Flask
import pathlib
import StateMachine.main as main

# Define Flask server
app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

if __name__ == '__main__':
    app.run(host='172.20.10.3', port=5000)
    main.main()