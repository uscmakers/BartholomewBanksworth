<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>README</title>
<style>
  body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
  }
  h1 {
    font-size: 24px;
    margin-bottom: 10px;
  }
  h2 {
    font-size: 20px;
    margin-top: 20px;
    margin-bottom: 10px;
  }
  code {
    background-color: #f4f4f4;
    border: 1px solid #ddd;
    border-radius: 4px;
    display: block;
    margin: 10px 0;
    padding: 10px;
  }
</style>
</head>
<body>

<h1>TO RUN CODE IN StateMachine:</h1>

<ol>
  <li>
    <code>cd StateMachine</code>
    <br>
    <code>python3 main.py</code>
  </li>
</ol>

<h1>TO RUN CODE IN SIMPLEv1:</h1>

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
