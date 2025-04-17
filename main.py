#MapPlot.py
#Name:Juan V Mancilla Vargas
#Date:04/17/2025
#Assignment: Lab 10- Visualizations with Mathplotlib



# MapPlot.py
# Name: Juan V Mancilla Vargas
# Date: 04/17/2025
# Assignment: Lab 10 - Visualizations with Matplotlib


import pandas
import matplotlib.pyplot as plt

import construction_spending
spending = construction_spending.get_spending()


years = []
values = []


for item in spending:
    year = item["time"]["year"]
    value = item["annual"]["combined"]["commercial"]
   
    if value != 0:
        years.append(year)
        values.append(value)


df = pandas.DataFrame({
    "Year": years,
    "Commercial Spending": values
})


print(df)


df.plot(kind="line", x="Year", y="Commercial Spending")
plt.savefig("output")


