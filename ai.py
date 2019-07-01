from pypokerengine.api.game import setup_config, start_poker
from fish_player import FishPlayer
from honest_player import HonestPlayer
import config

engine_config = setup_config(
    max_round=config.num_rounds,
    initial_stack=config.initial_stack,
    small_blind_amount=config.small_blind_amount
)
engine_config.register_player(name="p1", algorithm=FishPlayer())
engine_config.register_player(name="p2", algorithm=HonestPlayer())
game_result = start_poker(engine_config, verbose=1)

print("Game result: " + str(game_result))
