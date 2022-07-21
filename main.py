import csv
import itertools


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
            action_benefit = int(action_price)*int(action_profit)/100

            new_action = Action(action_name, action_price, action_profit, action_benefit)
            list_actions.append(new_action)
    return list_actions

            #print(new_action.__dict__)

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
            globalCost = int(globalCost) + int(eachAction.action_price)
        if int(globalCost) <= 500:
            investment500.append(eachList)
            #print(eachList)
        else: pass
    return investment500

def select_best_profit(selectInvestment):
    bestBenefitAction = []
    for eachInvestment in selectInvestment:
        bestBenefit = 0
        #print(eachInvestment)
        for actions in eachInvestment:
            bestBenefit = int(bestBenefit) + int(actions.action_benefit)
        if bestBenefit > 0:
            bestBenefitAction.append(max(bestBenefit))
        else: pass
    print(bestBenefitAction)

if __name__ == '__main__':

    list_actions = transform_csv_to_obj()
    totalCombination = search_combination(list_actions)
    #combinations_investment500(totalCombination)
    investment500 = combinations_investment500(totalCombination)
    select_best_profit(investment500)
