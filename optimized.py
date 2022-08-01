import csv
import time


max_invest = 500


class Action:
    def __init__(self, action_name, action_price, action_profit, action_benefit):
        self.action_name = action_name
        self.action_price = action_price
        self.action_profit = action_profit
        self.action_benefit = action_benefit


def transform_csv_to_obj():
    list_actions = []
    with open('actions.csv') as file:
        obj_csv = csv.reader(file, delimiter=',')
        next(obj_csv)
        for action in obj_csv:
            action_name = action[0]
            action_price = action[1]
            action_profit = action[2]
            action_benefit = int(action_price) * int(action_profit)

            new_action = Action(action_name, action_price, action_profit, action_benefit)
            list_actions.append(new_action)
    return list_actions


def optimized_investment(max_invest, list_actions):
    matrice = [[0 for x in range(max_invest + 1)] for x in range(len(list_actions) + 1)]

    for i in range(1, len(list_actions) + 1):
        for w in range(1, max_invest + 1):
            if int(list_actions[i-1].action_price) <= w:
                matrice[i][w] = max(int(list_actions[i-1].action_benefit) + matrice[i-1]
                [w - int(list_actions[i-1].action_price)], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    w = max_invest
    n = len(list_actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        if matrice[n][w] == matrice[n-1][w - int(list_actions[n-1].action_price)] + int(list_actions[n-1].action_benefit):
            actions_selection.append(list_actions[n-1])
            w -= int(list_actions[n-1].action_price)
        n -= 1
    return matrice[-1][-1], actions_selection


if __name__ == '__main__':


    start_time = time.time()
    list_actions = transform_csv_to_obj()
    optimized_investment(max_invest, list_actions)
    actions_selection = optimized_investment(max_invest, list_actions)
    print(actions_selection[0] / 100)
    for x in actions_selection[1]: print(x.__dict__)
    print("--- %s secondes ---" % (time.time() - start_time))
