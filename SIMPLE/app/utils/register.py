

def get_environment(env_name):
    try:
        #print("ajsdnkkjsdbj")
        if env_name in ('tictactoe'):
            from tictactoe.envs.tictactoe import TicTacToeEnv
            return TicTacToeEnv
        elif env_name in ('connect4'):
            from connect4.envs.connect4 import Connect4Env
            return Connect4Env
        elif env_name in ('sushigo'):
            from sushigo.envs.sushigo import SushiGoEnv
            return SushiGoEnv
        elif env_name in ('butterfly'):
            from butterfly.envs.butterfly import ButterflyEnv
            return ButterflyEnv
        elif env_name in ('geschenkt'):
            from geschenkt.envs.geschenkt import GeschenktEnv
            return GeschenktEnv
        elif env_name in ('frouge'):
            from frouge.envs.frouge import FlammeRougeEnv
            return FlammeRougeEnv
        elif env_name in ('monopoly'):
            print("try block under monpoly")
            from monopoly.envs.monopoly import MonopolyEnv
            print("checking after from before return")
            return MonopolyEnv
        else:
            print("checking else")
            raise Exception(f'No environment found for {env_name}')
    except SyntaxError as e:
        print(e)
        raise Exception(f'Syntax Error for {env_name}!')
    except:
        raise Exception(f'Install the environment first using: \nbash scripts/install_env.sh {env_name}\nAlso ensure the environment is added to /utils/register.py')
    


def get_network_arch(env_name):
    print("hellooooooo")
    if env_name in ('tictactoe'):
        from models.tictactoe.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('connect4'):
        from models.connect4.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('sushigo'):
        from models.sushigo.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('butterfly'):
        from models.butterfly.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('geschenkt'):
        from models.geschenkt.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('frouge'):
        from models.frouge.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('monopoly'):

        from models.monopoly.models import CustomPolicy
        print("network check")
        return CustomPolicy
    else:
        raise Exception(f'No model architectures found for {env_name}')

