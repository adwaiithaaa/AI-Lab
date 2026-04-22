from itertools import permutations

letters = "SENDMORY"

digits = range(10)

# Try all possible assignments
for perm in permutations(digits, len(letters)):
    d = dict(zip(letters, perm))
    
    # Leading digit constraint
    if d['S'] == 0 or d['M'] == 0:
        continue
    
    # Form numbers
    SEND = d['S']*1000 + d['E']*100 + d['N']*10 + d['D']
    MORE = d['M']*1000 + d['O']*100 + d['R']*10 + d['E']
    MONEY = d['M']*10000 + d['O']*1000 + d['N']*100 + d['E']*10 + d['Y']
    
    # Check equation
    if SEND + MORE == MONEY:
        print("Solution found:")
        print(d)
        print(f"{SEND} + {MORE} = {MONEY}")
        break