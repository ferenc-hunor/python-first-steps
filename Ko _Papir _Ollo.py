import random

hand_to_value = ('kő', 'papír', 'olló')
delta_to_result = {0: 'egyenlő'}

print("Válassz egyet az alábbiakból és írd be a számát:\n"
      "1.: kő\n"
      "2.: papír\n"
      "3.: olló\n")

# TODO: validate user input
user_hand = input("A te számod: ")
print(f'A te kezed: {hand_to_value[int(user_hand)-1]}')
cpu_value = random.choice(hand_to_value)
print(f'A gép keze: {cpu_value}')
cpu_hand = hand_to_value.index(cpu_value)
