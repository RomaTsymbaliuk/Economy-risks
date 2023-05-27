import random

risk_list = ["Team extending", "Price of product increasing", "Microchips price increasing", "Terms of programms decreasing", "New bugs appearing", "Electricity blackout", "New concurents appearing", "Minimal salary raising", "New features implementing, product stability integrating"]

experts_grades = {}
num_experts = 5

def experts_grades_generate(num_experts):
    for risk in risk_list:
        experts_grades[risk] = [random.randint(1,10) for x in range(num_experts)]

experts_grades_generate(num_experts)
print(experts_grades)
