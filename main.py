import csv
import itertools

list_actions = []

class Action:
    def __init__(self, action_name, action_price, action_profit, action_benefit):
        self.action_name = action_name
        self.action_price = action_price
        self.action_profit = action_profit
        self.action_benefit = action_benefit

def transform_csv_to_obj():
    with open('actions.csv') as file:
        obj_csv = csv.reader(file, delimiter=',')
        next(obj_csv)
        for action in obj_csv:
            action_name = action[0]
            action_price = action[1]
            action_profit = action[2]
            action_benefit = int(action_price)*int(action_profit)/100

            new_action = Action(action_name, action_price, action_profit, action_benefit)
            list_actions.append(new_action)

            #print(new_action.__dict__)

def search_combinaison(list_actions):
    totalCombination = []
    for i in range(len(list_actions)):
        combination = itertools.combinations(list_actions, i)
        for combo in combination:
            totalCombination.append(combo)
            print(combo)
    return totalCombination


if __name__ == '__main__':

    transform_csv_to_obj()
    search_combinaison(list_actions)
# + condition max 500euros