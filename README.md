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
  <li><code>docker-compose exec app python3 train.py -r -e monopoly</code></li>
  <li>To test with one human player and one AI, run:</li>
  <li><code>docker-compose exec app python3 test.py -d -g 1 -a base human -e monopoly</code></li>
  <li>To test with two AI players, run:</li>
  <li><code>docker-compose exec app python3 test.py -d -g 1 -a base base -e monopoly</code></li>
</ol>

<h1>To run code in StateMachinePhysical:</h1>

<p>On a Raspberry Pi:</p>
<ol>
  <li><code>git clone git@github.com:uscmakers/BartholomewBanksworth.git</code></li>
  <li><code>cd BartholomewBanksworth/StateMachinePhysical/Embedded</code></li>
  <li><code>python3 server.py</code></li>
</ol>

<p>On local machine:</p>
<ol>
  <li><code>cd StateMachinePhysical</code></li>
  <li><code>python3 main.py</code></li>
</ol>

<h1>To run code in StateMachinePhysicalAIv2:</h1>

<p>On a Raspberry Pi:</p>
<ol>
  <li><code>git clone git@github.com:uscmakers/BartholomewBanksworth.git</code></li>
  <li><code>cd BartholomewBanksworth/StateMachinePhysicalAIv2/app/Embedded</code></li>
  <li><code>python3 server.py</code></li>
</ol>

<p>On local machine: [Windows or Intel Mac required]</p>
<ol>
  <li>Install Docker and Docker Compose</li>
  <li><code>cd StateMachinePhysicalAIv2</code></li>
  <li><code>docker-compose up -d</code></li>
  <li><code>bash ./scripts/install_env.sh monopoly</code></li>
  <li>For 2 players: <code>docker-compose exec app python3 test.py -g 1 -a base2 human -e monopoly</code></li>
  <li>For 3 players: <code>docker-compose exec app python3 test.py -g 1 -a base3 base3 human -e monopoly</code></li>
  <li>For 4 players: <code>docker-compose exec app python3 test.py -g 1 -a base4 base4 base4 human -e monopoly</code></li>
</ol>

</body>
</html>
