# This code compares coronavirus
# infection rates across countries, pseudocode included in comments
import numpy as np
import matplotlib.pyplot as plt
# construct a dictionary to store data
dict_of_cases = {"USA": 29862124, "India": 11285561,
                 "Brazil": 11205972, "Russia": 4360823,
                 "UK": 4234924}
# print the dictionary as output
print(dict_of_cases)
# turn values & keys in dict_of_cases into 2 arrays
data = np.array([i for i in dict_of_cases.values()])
labels = np.array([j for j in dict_of_cases.keys()])
# draw the pie chart as output
plt.pie(data, labels=labels, shadow=True)
plt.title("Coronavirus Infection Rates across Countries")
plt.show()
