import random

def bot_choise(player: str) -> str:
    bot = random.choice(['🪨', '✂️', '📄'])
    if bot == player:
        return (bot, 'draw')
    elif (bot == '🪨' and player == '✂️') or (bot == '✂️' and player == '📄') or (bot == '📄' and player == '🪨'):
        return (bot, 'loss')
    else:
        return (bot, 'victory')