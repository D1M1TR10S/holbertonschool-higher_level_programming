#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    highscore = 0
    for key in my_dict:
        if my_dict[key] > highscore:
            highscore = my_dict[key]
            best = key
    return best
