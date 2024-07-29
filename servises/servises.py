import random

def bot_choise(player: str) -> str:
    bot = random.choice(['🪨', '✂️', '📄'])
    if bot == player:
        return (bot, 'draw')
    elif (bot == '🪨' and player == '✂️') or (bot == '✂️' and player == '📄') or (bot == '📄' and player == '🪨'):
        return (bot, 'victory')
    else:
        return (bot, 'loss')


def bot_answer(result: str, base_answers: dict) -> str:
    answer = random.choice(base_answers[result])
    return answer