from gym.envs.registration import register

register(
    id='Monopoly-v0',
    entry_point='monopoly.envs:MonopolyEnv',
)