<!DOCTYPE html>
<html lang="en">

<body>

<h1>To run code in StateMachine:</h1>

<ol>
  <li>
    <code>cd StateMachine</code>
    <br>
    <code>python3 main.py</code>
  </li>
</ol>

<h1>To run code in SIMPLEv1:</h1>

<ol>
  <li>Install Docker and Docker Compose</li>
  <li>
    <code>cd SIMPLEv1</code>
    <br>
    <code>docker-compose up -d</code>
    <br>
    <code>bash ./scripts/install_env.sh monopoly</code>
  </li>
  <li>To train, run:</li>
  <code>docker-compose exec app python3 train.py -r -e monopoly</code>
  <li>To test with one human player and one AI, run:</li>
  <code>docker-compose exec app python3 test.py -d -g 1 -a base human -e monopoly</code>
  <li>To test with two AI players, run:</li>
  <code>docker-compose exec app python3 test.py -d -g 1 -a base base -e monopoly</code>
</ol>

</body>
</html>

test
