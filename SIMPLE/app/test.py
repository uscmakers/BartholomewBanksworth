# docker-compose exec app python3 test.py -d -g 1 -a base base human -e butterfly 

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
tf.get_logger().setLevel('INFO')
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

import random
import argparse

from stable_baselines import logger
from stable_baselines.common import set_global_seeds

from utils.files import load_model, write_results
from utils.register import get_environment
from utils.agents import Agent

import config

from constants import property_stuff, const

def main(args):

  logger.configure(config.LOGDIR)

  if args.debug:
    logger.set_level(config.DEBUG)
  else:
    logger.set_level(config.INFO)
    
  #make environment
  env = get_environment(args.env_name)(verbose = args.verbose, manual = args.manual)
  env.seed(args.seed)
  set_global_seeds(args.seed)

  total_rewards = {}

  if args.recommend:
    ppo_model = load_model(env, 'best_model.zip')
    ppo_agent = Agent('best_model', ppo_model)
  else:
    ppo_agent = None


  agents = []

  #load the agents
  # if len(args.agents) != env.n_players:
  #   raise Exception(f'{len(args.agents)} players specified but this is a {env.n_players} player game!')

  for i, agent in enumerate(args.agents):
    if agent == 'human':
      agent_obj = Agent('human')
    elif agent == 'rules':
      agent_obj = Agent('rules')
    elif agent == 'base':
      base_model = load_model(env, 'base.zip')
      agent_obj = Agent('base', base_model)   
    else:
      ppo_model = load_model(env, f'{agent}.zip')
      agent_obj = Agent(agent, ppo_model)
    agents.append(agent_obj)
    total_rewards[agent_obj.id] = 0
  
  #play games
  logger.info(f'\nPlaying {args.games} games...')
  for game in range(args.games):
    players = agents[:]

    if args.randomise_players:
      random.shuffle(players)

    obs = env.reset()
    done = False
    
    for i, p in enumerate(players):
      logger.debug(f'Player {i+1} = {p.name}')

    while not done:

      current_player = players[env.current_player_num]
      env.render()
      logger.debug(f'\nCurrent player name: {current_player.name}')

      if args.recommend and current_player.name in ['human', 'rules']:
        # show recommendation from last loaded model
        logger.debug(f'\nRecommendation by {ppo_agent.name}:')
        action = ppo_agent.choose_action(env, choose_best_action = True, mask_invalid_actions = True)

      player = env.current_player
      if current_player.name == 'human':
        action = -1
        if player.mTurnsInJail > 0: # in-jail check
            print(player.mPlayerName + " is in jail!")
            if player.mNumJailFree > 0: # get out of jail free card
              choice = input("Would you like to use your get out of jail free card? (yes/no) ")
              if choice == "yes":
                  # player.UseGetOutOfJailFree()
                  action = 29
            elif player.mBalance >= const.JAIL_FEE:
              choice = input("Would you like to pay the $" + str(const.JAIL_FEE) + " jail fee? (yes/no) ")
              if choice == "yes":
                  # player.PayJailFee()
                  #print("made it here!")
                  action = 30
        else:
          rolled = True
          while True:  
              command = input("Type a command, or type help: ")
              if command == "help":
                  env.helpMenu()
              elif command == "end":
                  if rolled: 
                      # os.system('clear')
                      break
                  print("You haven't rolled yet!")
              elif command == "roll":
                  if rolled:
                      print("You already rolled!")
                  else:
                      rolled = True
                      action = env.turn(env.current_player_num)
                      if action != 0: break # only allow the player to make one decision per turn (cannot build AND purchase in the same turn)
              elif command == "stats":
                  env.stats(env.current_player_num)
              # TODO: future implementation
              elif command == "build":
                  # pick property to build on from property list
                  if (not(len(player.mDeedOwned) == 0)):
                    count: int = 1
                    for d in player.mDeedOwned:
                        if d.mSet != "utility" and d.mSet != "railroad":
                            print(str(count) + ". " + str(d.mTileName)) 
                        else:
                            print(str(count) + ". " + str(d.mTileName) + " (can not build house)")
                        count += 1
                    select = int(input("Enter corresponding number to select property: "))
                    developProperty: property = player.mDeedOwned[select - 1]
                    # check if can build on selected property
                    if player.mBalance >= developProperty.mHouseCost and developProperty.BuildHouse(player):
                        # if can build, check if enough balance, then build, increment house count
                        ans = input("Do you want to build here (y/n)? ")
                        if ans in "Yy":
                            # developProperty.mNumHouse += 1
                            # if developProperty.mNumHouse == 5: player.mHotelOwned += 1
                            # else: player.mHouseOwned += 1
                            print("You have built a house")
                            action = property_stuff.Deeds.index(developProperty) + 1
                    else:
                        print("Cannot build a house here.")
                  else:
                     print("No properties")
              elif command == "quit":
                  ans = input("Are you sure you want to quit the game? Your progress won't be saved. (y/n) ")
                  if ans in "Yy":
                      env.reset()
                      return
              else:
                  print("Not a valid command. Type help to see list of valid commands.")
        try:
          # for int actions
          action = int(action)
        except:
          # for MulitDiscrete action input as list TODO
          action = eval(action)
      elif current_player.name == 'rules':
        logger.debug(f'\n{current_player.name} model choices')
        action = current_player.choose_action(env, choose_best_action = False, mask_invalid_actions = True)
      else: # current_player.name == 'base'
        env.turn(env.current_player_num)
        logger.debug(f'\n{current_player.name} model choices')
        action = current_player.choose_action(env, choose_best_action = args.best, mask_invalid_actions = True)

      obs, reward, done, _ = env.step(action)

      for r, player in zip(reward, players):
        total_rewards[player.id] += r
        player.points += r

      if args.cont:
        input('Press any key to continue')
    
    env.render()

    logger.info(f"Played {game + 1} games: {total_rewards}")

    if args.write_results:
      write_results(players, game, args.games, env.turns_taken)

    for p in players:
      p.points = 0

  env.close()
    


def cli() -> None:
  """Handles argument extraction from CLI and passing to main().
  Note that a separate function is used rather than in __name__ == '__main__'
  to allow unit testing of cli().
  """
  # Setup argparse to show defaults on help
  formatter_class = argparse.ArgumentDefaultsHelpFormatter
  parser = argparse.ArgumentParser(formatter_class=formatter_class)

  parser.add_argument("--agents","-a", nargs = '+', type=str, default = ['human', 'human']
                , help="Player Agents (human, ppo version)")
  parser.add_argument("--best", "-b", action = 'store_true', default = False
                , help="Make AI agents choose the best move (rather than sampling)")
  parser.add_argument("--games", "-g", type = int, default = 1
                , help="Number of games to play)")
  # parser.add_argument("--n_players", "-n", type = int, default = 3
  #               , help="Number of players in the game (if applicable)")
  parser.add_argument("--debug", "-d",  action = 'store_true', default = False
            , help="Show logs to debug level")
  parser.add_argument("--verbose", "-v",  action = 'store_true', default = False
            , help="Show observation on debug logging")
  parser.add_argument("--manual", "-m",  action = 'store_true', default = False
            , help="Manual update of the game state on step")
  parser.add_argument("--randomise_players", "-r",  action = 'store_true', default = False
            , help="Randomise the player order")
  parser.add_argument("--recommend", "-re",  action = 'store_true', default = False
            , help="Make recommendations on humans turns")
  parser.add_argument("--cont", "-c",  action = 'store_true', default = False
            , help="Pause after each turn to wait for user to continue")
  parser.add_argument("--env_name", "-e",  type = str, default = 'TicTacToe'
            , help="Which game to play?")
  parser.add_argument("--write_results", "-w",  action = 'store_true', default = False
            , help="Write results to a file?")
  parser.add_argument("--seed", "-s",  type = int, default = 17
            , help="Random seed")

  # Extract args
  args = parser.parse_args()

  # Enter main
  main(args)
  return


if __name__ == '__main__':
  cli()