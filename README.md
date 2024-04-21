# BartholomewBanksworth

TO RUN CODE IN StateMachine:

1. 
cd StateMachine
python3 main.py

TO RUN CODE IN SIMPLEv1:

1. Install Docker and Docker Compose

2. 
cd SIMPLEv1
docker-compose up -d
bash ./scripts/install_env.sh monopoly

3. To train, run: 
docker-compose exec app python3 train.py -r -e monopoly

4. To test with one human player and one AI, run:
docker-compose exec app python3 test.py -d -g 1 -a base human -e monopoly

5. To test with two AI players, run:
docker-compose exec app python3 test.py -d -g 1 -a base base -e monopoly