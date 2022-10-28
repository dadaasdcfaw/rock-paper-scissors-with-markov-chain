# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

print("QUINCY")
play(player, quincy, 100)
print("\nABBEY")
play(player, abbey, 100)
print("\nkris")
play(player, kris, 100)
print("\nmrugesh")
play(player, mrugesh, 100)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)