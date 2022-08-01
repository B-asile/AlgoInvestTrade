import csv
import itertools
import time


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


def search_combination(list_actions):
    totalCombination = []
    for i in range(len(list_actions)):
        combination = itertools.combinations(list_actions, i)
        for combo in combination:
            totalCombination.append(combo)
            # print(combo)
    return totalCombination


def combinations_investment500(eachCombination):
    investment500 = []
    for eachList in eachCombination:
        globalCost = 0
        for eachAction in eachList:
            globalCost = float(globalCost) + float(eachAction.action_price)
        if float(globalCost) <= 500:
            investment500.append(eachList)
        else: pass
    return investment500


def select_best_profit(selectInvestment):
    bestBenefit = 0
    bestList = 0
    for eachInvestment in selectInvestment:
        curentBenefit = 0
        for actions in eachInvestment:
            curentBenefit = float(curentBenefit) + float(actions.action_benefit)
            if curentBenefit > bestBenefit:
                bestBenefit = curentBenefit
                bestList = eachInvestment
            else: pass
    print(f"la combinaison d'actions avec le meilleur rendement en terme de benefice est de :{bestBenefit} euros ")
    print(f"________lot d'actions_______")
    for i in bestList:
        print(i.__dict__)
    return bestBenefit, bestList


if __name__ == '__main__':

    start_time = time.time()
    list_actions = transform_csv_to_obj()
    totalCombination = search_combination(list_actions)
    investment500 = combinations_investment500(totalCombination)
    select_best_profit(investment500)
    print("--- %s secondes ---" % (time.time() - start_time))
