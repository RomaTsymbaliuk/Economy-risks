import random
import math

risk_list = ["Team extending", "Price of product increasing", "Microchips price increasing", "Terms of programms decreasing", "New bugs appearing", "Electricity blackout", "New concurents appearing", "Minimal salary raising", "New features implementing, product stability integrating"]

experts_grades = {}
num_experts = 5
sum_index = num_experts
L_index = sum_index + 1
L_squared_index = L_index + 1

def experts_grades_generate(num_experts):
    for risk in risk_list:
        experts_grades[risk] = [random.randint(1,10) for x in range(num_experts)]

def average_calculate():
    col_summ = 0
    summ = 0
    for grade_key in experts_grades:
        col_summ = sum(experts_grades[grade_key])
        experts_grades[grade_key].append(col_summ)
        summ = summ + col_summ
        col_summ = 0

    avg = summ / (len(risk_list))
    print("Average : ", avg)
    return avg

def L_calculate():
    avg = average_calculate()
    for grade_key in experts_grades:
        L = experts_grades[grade_key][sum_index] - avg
        experts_grades[grade_key].append(L)

def L_squared_calculate():
    for grade_key in experts_grades:
        L_squared = math.pow(experts_grades[grade_key][L_index], 2)
        experts_grades[grade_key].append(L_squared)

experts_grades_generate(num_experts)
L_calculate()
L_squared_calculate()

print(experts_grades)
