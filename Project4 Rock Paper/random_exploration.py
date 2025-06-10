import random

# coffee = random.randint(3, 8)
# sleep = random.randint(5, 11)
# game = random.randint(1, 4)
#
# print(f"I will drink {coffee} cups of coffee today and sleep for {sleep} hours tonight"
#       f" after playing {game} hours of Mario. Yeah!")

# Coin Flip
flip = random.randint(0, 1)
if flip == 0:
    print("Sonic")
else:
    print("Tails")


# Game List

game_list = ["Oblivion Remake", "Spiderman: Miles Morales", "FF: Stranger Of Paradise", "Yukae Laylee", "A Hat In Time"]

game_list[0] = "Cat Quest 2"
game_list.append("Two Point Hospital")
