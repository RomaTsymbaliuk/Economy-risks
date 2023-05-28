import random
import math
from decimal import *
from scipy.stats import *
import sys

risk_list = ["Team extending", "Price of product increasing", "Microchips price increasing", "Terms of programms decreasing", "New bugs appearing", "Electricity blackout", "New concurents appearing", "Minimal salary raising", "New features implementing, product stability integrating"]

experts_grades = {}
num_experts = int(sys.argv[1])
sum_index = num_experts
L_index = sum_index + 1
L_squared_index = L_index + 1

def print_experts_grades():
    for grade_key in experts_grades:
        string = "  ".join(f'{str(e):<5}' for e in experts_grades[grade_key])
        print(f"{grade_key : <70}{string : >30}")

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
        experts_grades[grade_key].append(round(L, 2))

def L_squared_calculate():
    for grade_key in experts_grades:
        L_squared = math.pow(experts_grades[grade_key][L_index], 2)
        experts_grades[grade_key].append(round(L_squared,2))

def Concordation_coeff():
    tv = 0
    sum_L_squared = 0
    for grade_key in experts_grades:
        sum_L_squared = sum_L_squared + experts_grades[grade_key][L_squared_index]
        for grade_key2 in experts_grades:
            if grade_key is not grade_key2 and experts_grades[grade_key][sum_index] == experts_grades[grade_key2][sum_index]:
                tv = tv + 1
    tv = tv / 2
    m = num_experts
    k = len(risk_list)
    n = m
    T = n * (tv * tv * tv - tv)
    print('sum_L_squared ', sum_L_squared)
    W = 12 * sum_L_squared / ((m * m) * (k * k * k - k) - m * T)
    print('W is ', W)
    return W

def pirson_calculate(W):
    pirson = num_experts * (len(risk_list) - 1) * W
    print('Calculated pirson ', pirson)
    return pirson

def compare_pirson(pirson_calculated, probability):
    critical_value= chi2.ppf(q = probability, df = (len(risk_list) - 1))
    print('critical value ', critical_value)
    if pirson_calculated < critical_value:
       print('-------------------------------')
       print('Extend number of experts')
    else:
        print('------------------------------')
        print('Calculated pirson is bigger then table pirson. Seems fine')

    
experts_grades_generate(num_experts)
L_calculate()
L_squared_calculate()
print_experts_grades()

W = Concordation_coeff()
pirson_calculated = pirson_calculate(W)
compare_pirson(pirson_calculated, 0.85)
