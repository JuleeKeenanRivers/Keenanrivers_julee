import random
player = random.randint(1,6)
computer = random.randint(1,6)

print("You rolled a: ", player)
print("computer rolled a: ", computer)

if player > computer:
    print("Winner is you")
if computer > player:
    print("Winner is computer")
    
