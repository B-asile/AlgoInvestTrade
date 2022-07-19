import csv

list_actions = []
benefit = []


class Action:
    def __init__(self, action_name, action_price, action_profit):
        self.action_name = action_name
        self.action_price = action_price
        self.action_profit = action_profit


def transform_csv_to_obj():
    with open('actions.csv') as file:
        obj_csv = csv.reader(file, delimiter=',')
        next(obj_csv)
        for action in obj_csv:
            action_name = action[0]
            action_price = action[1]
            action_profit = action[2]

            new_action = Action(action_name, action_price, action_profit)
            list_actions.append(new_action)

            #print(new_action.__dict__)

#calcule benefice pour chaques actions
def profit_for_actions():
    for action in list_actions:
        benefit.append(int(action.action_price) * int(action.action_profit) / 100)
    print(benefit)

#tri décroissant
#ajout des actions coût <= 500

if __name__ == '__main__':

    transform_csv_to_obj()
    profit_for_actions()
