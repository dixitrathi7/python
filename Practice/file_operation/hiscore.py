
import random

def game():
    score = random.randint(0, 100)

    with open("hiscore.txt", 'r') as f:
        hiscore = f.read()

    hiscore = int(hiscore) if hiscore else 0

    if score > hiscore or hiscore == 0:
        with open("hiscore.txt", 'w') as f:
            f.write(str(score))
        print(f"New high score! Your score: {score}")
    else:
        print(f"Your score: {score}. High score remains: {hiscore}")

game()
