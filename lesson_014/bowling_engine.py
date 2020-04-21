from random import randint


PINS = 10
FRAME = 10


def bowling(*args):
    total_score = []
    for _ in range(FRAME):
        try_result = []
        remaining_pins = PINS
        throw_bowling_ball_try = 1
        while remaining_pins > 0 <= 10 and throw_bowling_ball_try <= 2:
            throw = randint(0, remaining_pins)
            remaining_pins -= throw
            throw_bowling_ball_try += 1
            if throw == 10:
                try_result.append(20)
            elif remaining_pins == 0:
                try_result.append(15 - try_result[0])
            else:
                try_result.append(throw)
        total_score.append(sum(try_result))
    print('всего очков', sum(total_score))
