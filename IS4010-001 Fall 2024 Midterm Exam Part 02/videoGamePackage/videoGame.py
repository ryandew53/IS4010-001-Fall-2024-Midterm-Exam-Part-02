# videoGame.py


import random
def play():
    '''
    Simulate a really bad video game
    @return bool: True if you won, False if you lost 
    '''
    if random.randint(0,100) == 10:
        raise Exception("Game Crashed")
    return random.choice([True, False])
