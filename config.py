import os
import logging


log_file = "hearts_ai.log"
try:
    os.remove(log_file)
except:
    pass
logging.basicConfig(filename=log_file, level=logging.DEBUG)
logging.disable(logging.DEBUG)

num_players = 2
initial_stack = 200
small_blind_amount = 1
num_rounds = 10
