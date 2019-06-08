# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 01:45:02 2018

@author: NAO
"""
from copy import deepcopy
import random as rand
import matplotlib.pyplot as plt
import time
rand.seed(time.time())

def proj1(days, people, save_data):
    for x in range(days):
        for y in range(len(people)):
            people[y] = people[y] - 1
            z = rand.randrange(0, len(people))
            people[z] = people[z] + 1
        save_data[x + 1] = deepcopy(people)
        
def print_graph(day_number, people, save_data):
    plt.bar(range(len(people)), save_data[day_number], align='center', color = ['r'])
    plt.xticks(range(len(people)))
    plt.tight_layout()
    plt.legend()
    plt.title('Who Could be Rich?')
    plt.xlabel('Person')
    plt.ylabel('Dollars')
    plt.show()
    
    
days = 50
cash = 50
people = []
for h in range(50):
    people.append(cash)
save_data = [[]] * (len(people) + 1)
save_data[0] = deepcopy(people)
proj1(days, people, save_data)
print_graph(50, people, save_data)
print(save_data[50])