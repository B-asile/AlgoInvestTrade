import csv
import time


def file_choice():
    print("choisissez un fichier à analyser :\n"
          "1 - pour actions.csv\n"
          "2 - pour dataset1_Python+P7.csv\n"
          "3 - pour dataset1_Python+P7.csv\n")
    while True:
        user_select = input("saisissez le N° correspondant au fichier de votre choix:")
        if user_select == "1":
            return "actions.csv"
        elif user_select == "2":
            return "dataset1_Python+P7.csv"
        elif user_select == "3":
            return "dataset2_Python+P7.csv"
        else:
            print("saisie incorrect")


def transform_csv(file_name):
    list_actions = []
    precision = 100

    with open(file_name) as file:
        obj_csv = csv.DictReader(file, delimiter=',')
        for row in obj_csv:
            if (float(row["price"])) > 0 and (float(row["profit"])) > 0:
                action = (row["name"], int(float(row["price"])*precision), int(float(row["profit"])*precision), int(float(row["price"])*precision) * int(float(row["profit"])*precision))
                list_actions.append(action)
                max_invest = 500 * precision
    return list_actions, max_invest


# O(NW)
def optimized_investment(max_invest, list_actions):
    matrice = [[0 for x in range(max_invest + 1)] for x in range(len(list_actions) + 1)]
    for i in range(1, len(list_actions) + 1):
        for w in range(1, max_invest + 1):
            if list_actions[i - 1][1] <= w:
                matrice[i][w] = max((list_actions[i-1][3]) + matrice[i-1]
                [w - list_actions[i - 1][1]], matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    w = max_invest
    n = len(list_actions)
    actions_selection = []


    while w >= 0 and n >= 0:
        if matrice[n][w] == matrice[n - 1][w - list_actions[n - 1][1]] + list_actions[n - 1][3]:
            actions_selection.append(list_actions[n-1])
            w -= list_actions[n - 1][1]
        n -= 1

    share_packages_price = sum([list_actions[1] for list_actions in actions_selection])

    return matrice[-1][-1], actions_selection, share_packages_price


if __name__ == '__main__':


    user_choice = file_choice()
    list_actions, max_invest = transform_csv(user_choice)
    start_time = time.time()
    matrice, actions_selection, share_packages_price = optimized_investment(max_invest, list_actions)
    print(f"le meilleur rendement en terme de benefice est de: {matrice / 10000}")
    print(f"Pour un investissement de:{float(share_packages_price) / 10}")
    print(f"------lot d'actions-------")
    for x in actions_selection:
        print(x[0], float(x[1]/100), float(x[2]/100), float(x[3]/100000))
    print("--- %s secondes ---" % (time.time() - start_time))
