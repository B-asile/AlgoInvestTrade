import csv


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
            action_benefit = float(action_price) * float(action_profit) / 100

            new_action = Action(action_name, action_price, action_profit, action_benefit)
            list_actions.append(new_action)
    return list_actions


def optimized_investment(max_invest, list_actions):
    matrice = [[0 for x in range(max_invest + 1)] for x in range(len(list_actions) + 1)]

    for i in range(1, len(list_actions) + 1):
        for w in range(1, max_invest + 1):
            print(list_actions[i-1].action_price)
            if list_actions[i-1].action_price[1] <= w:
                matrice[i][w] = max(list_actions[i-1][2] + matrice[i-1][w-list_actions[i-1][1]], matrice[i-1][w])
                print("if")
            else:
                matrice[i][w] = matrice[i-1][w]
                print("else")

    w = max_invest
    n = len(list_actions)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = list_actions[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1
    return matrice[-1][-1], elements_selection


if __name__ == '__main__':
    list_actions = transform_csv_to_obj()
    optimized_investment(max_invest, list_actions)
