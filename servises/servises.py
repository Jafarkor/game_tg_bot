import random
things: dict[str, str] = {'1': '🪨', '2': '✂️', '3': '📄'}

def bot_choise(player: str) -> str:
    bot = things[str(random.randint(1, 3))]
    if bot == player:
        return (bot, 'draw')
    elif (bot == '🪨' and player == '✂️') or (bot == '✂️' and player == '📄') or (bot == '📄' and player == '🪨'):
        return (bot, 'loss')
    else:
        return (bot, 'victory')