import itertools
rules = {"Life":{"B":[3], "S":[2,3]},
"HighLife":{"B":[3,6], "S":[2,3]},
"Day_and_Night":{"B":[3,6,7,8], "S":[3,4,6,7,8]},
"Diamoeba":{"B":[3,5,6,7,8], "S":[5,6,7,8]},
"LongLife":{"B":[3,4,5], "S":[5]}
}
iter_rule = itertools.cycle(rules)
game = "Life"
def Next():
    global game
    game = next(iter_rule)
    return rules[game]