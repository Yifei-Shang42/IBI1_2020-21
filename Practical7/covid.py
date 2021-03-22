# import packages
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# change directory
os.chdir("C:\\Users\\surface\\Desktop\\ZJU\\IBI")

# import .csv file
covid_data = pd.read_csv("full_data.csv")

# show all columns
covid_data.info()

# show every second row between 0 and 10
covid_data.iloc[0:10:2, 0:]

# total cases for rows of Afghanistan
def gen_country_boolean_list(country):
    country_booleans = []
    for row in covid_data.iloc[0:,1]:
        if row == country:
            country_booleans.append(True)
        else:
            country_booleans.append(False)
    return country_booleans
afgnst_booleans = gen_country_boolean_list("Afghanistan")
afghanistan_total_cases = covid_data.loc[afgnst_booleans,"total_cases"]
print(afghanistan_total_cases)

# compute mean & median of world new cases
    # generate boolean list
world_booleans = gen_country_boolean_list("World")
    # compute using boolean list
world_new_cases = covid_data.loc[world_booleans, "new_cases"]
mean = np.mean(world_new_cases)
median = np.median(world_new_cases)
print(mean)
print(median)

# plot boxplot of new cases worldwide
plt.boxplot(world_new_cases)
plt.show()

# plot new cases worldwide
world_dates = covid_data.loc[my_booleans, "date"]
plt.title("New Cases Worldwide")
plt.plot(world_dates, world_new_cases, 'ro', label="New Cases")
plt.legend()
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)


# plot new deaths worldwide
world_new_deaths = covid_data.loc[world_booleans, "new_deaths"]
plt.title("New Deaths Worldwide")
plt.plot(world_dates, world_new_deaths, 'bo', label="New Deaths")
plt.legend()
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)

# plot new cases in China & United Kingdom
china_booleans = gen_country_boolean_list("China")
china_new_cases = covid_data.loc[china_booleans, "new_cases"]
china_dates = covid_data.loc[china_booleans, "date"]

uk_booleans = gen_country_boolean_list("United Kingdom")
uk_new_cases = covid_data.loc[uk_booleans, "new_cases"]
uk_dates = covid_data.loc[uk_booleans, "date"]

plt.title("New Cases in UK & China")
plt.plot(china_dates, china_new_cases, "ro", label="China")
plt.plot(uk_dates, uk_new_cases, "bo", label="United Kingdom")
plt.legend()
plt.xticks(uk_dates.iloc[0:len(uk_dates):4],rotation=-90)

# one more question: How have new cases and total cases developed over time in Spain?
spain_booleans = gen_country_boolean_list("Spain")
spain_new_cases = covid_data.loc[spain_booleans, "new_cases"]
spain_total_cases = covid_data.loc[spain_booleans, "total_cases"]
spain_dates = covid_data.loc[spain_booleans, "date"]

plt.title("New & Total Cases in Spain")
plt.plot(china_dates, spain_new_cases, "ro", label="New Cases")
plt.plot(uk_dates, spain_total_cases, "bo", label="Total Cases")
plt.legend()
plt.xticks(spain_dates.iloc[0:len(spain_dates):4],rotation=-90)
