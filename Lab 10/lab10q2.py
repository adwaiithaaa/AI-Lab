import numpy as np
import pandas as pd



# Goal test
def is_goal(state):
    _, a, b = state
    return a == 'Clean' and b == 'Clean'

def actions(state):
    return ['Suck', 'Left', 'Right']


def results(state, action):
    loc, a, b = state
    outcomes = []

    if action == 'Suck':
        if loc == 'A':
            # Clean A
            outcomes.append(('A', 'Clean', b))
            
            # Clean A and B
            outcomes.append(('A', 'Clean', 'Clean'))

            # If already clean → may become dirty
            if a == 'Clean':
                outcomes.append(('A', 'Dirty', b))

        elif loc == 'B':
            outcomes.append(('B', a, 'Clean'))
            outcomes.append(('B', 'Clean', 'Clean'))

            if b == 'Clean':
                outcomes.append(('B', a, 'Dirty'))

    elif action == 'Right':
        outcomes.append(('B', a, b))

    elif action == 'Left':
        outcomes.append(('A', a, b))

    return outcomes

def and_or_search(state, path=[]):
    if is_goal(state):
        return []

    if state in path:
        return None

    for action in actions(state):
        plan = and_search(results(state, action), path + [state])
        
        if plan is not None:
            return [action, plan]

    return None


def and_search(states, path):
    plans = []

    for s in states:
        plan = and_or_search(s, path)
        
        if plan is None:
            return None
        
        plans.append(plan)

    return plans


def print_plan(plan, indent=0):
    if plan == []:
        print("  " * indent + "Goal reached")
        return
    
    action = plan[0]
    print("  " * indent + f"Action: {action}")
    
    if len(plan) > 1:
        subplans = plan[1]
        
        for i, sub in enumerate(subplans):
            print("  " * (indent+1) + f"Outcome {i+1}:")
            print_plan(sub, indent + 2)


initial_state = ('A', 'Dirty', 'Dirty')

plan = and_or_search(initial_state)

print("Initial State:", initial_state)


print(plan,"\n")

print_plan(plan)