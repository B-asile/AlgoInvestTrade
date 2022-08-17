import csv
import time


#max_invest = 0


def file_choice():
    while True:
        print("choisissez un fichier à analyser :\n"
                "1 - pour actions.csv\n"
                "2 - pour dataset1_Python+P7.csv\n"
                "3 - pour dataset1_Python+P7.csv\n")
        user_select = input("saisissez le N° correspondant au fichier de votre choix:")
        if user_select == "1" or user_select == "2" or user_select == "3":
            return user_select
        print("saisie incorrect")


# class Action:
#     def __init__(self, action_name, action_price, action_profit, action_benefit):
#         self.action_name = action_name
#         self.action_price = action_price
#         self.action_profit = action_profit
#         self.action_benefit = action_benefit


def transform_csv_to_obj(choice):
    list_actions = []
    # max_invest = 0

    if choice == "1":
        with open('actions.csv') as file:
            obj_csv = csv.DictReader(file, delimiter=',')
            # next(obj_csv)
            for row in obj_csv:
                # action = (row["action_name"], int(row["action_price"]), int(row["action_profit"]))
                action = (row["name"], int(row["price"]), int(row["profit"]))
                list_actions.append(action)
                # benefit = (int(row["price"]) * int(row["profit"]))
                benefit = int(list_actions.price) * int(list_actions.profit)
                list_actions.append(benefit)
                print(list_actions)
            max_invest = 500
    else:
        if choice == "2":
            with open('dataset1_Python+P7.csv') as file:
                obj_csv = csv.reader(file, delimiter=',')
                next(obj_csv)
        elif choice == "3":
            with open('dataset2_Python+P7.csv') as file:
                obj_csv = csv.reader(file, delimiter=',')
                next(obj_csv)
                for row in obj_csv:
                    # if not '-' in row:
                    if (float(row[1])) > 0 and (float(row[2])) > 0:
                        max_invest = 50000
    return list_actions, max_invest


# O(n^W)
def optimized_investment(max_invest, list_actions):
    matrice = [[0 for x in range(max_invest + 1)] for x in range(len(list_actions) + 1)]

    for i in range(1, len(list_actions) + 1):
        for w in range(1, max_invest + 1):
            if int(list_actions[i-1].action_price) <= w:
                matrice[i][w] = max((list_actions[i-1].action_benefit) + matrice[i-1]
               # matrice[i][w] = max(int(list_actions[i - 1].action_benefit) + matrice[i - 1]
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


    #choice = file_choice()
    start_time = time.time()
    list_actions, max_invest = transform_csv_to_obj(file_choice())
    optimized_investment(max_invest, list_actions)
    actions_selection = optimized_investment(max_invest, list_actions)
    print(actions_selection[0] / 100)
    for x in actions_selection[1]:
        print(x.__dict__)
    print("--- %s secondes ---" % (time.time() - start_time))
