import requests
import pandas as pd
import matplotlib.pyplot as plt

url_gas_data = 'https://raw.githubusercontent.com/KeithGalli/matplotlib_tutorial/master/gas_prices.csv'
res1 = requests.get(url_gas_data, allow_redirects=True)

with open('gas_prices.csv', 'wb') as file:
    file.write(res1.content)

plt.figure(figsize=(12, 5))

gas = pd.read_csv('gas_prices.csv')

plt.title('Gas prices overtime (in USD)', fontdict={
'fontweight': 'bold', 'fontsize': 16
})


countries_to_look_at = ['USA', 'Australia', 'South Korea', 'Canada']
for country in gas:
    if country in countries_to_look_at:
        plt.plot(gas.Year, gas[country], label=country, marker='.')


"""
Other way to pass data:

plt.plot(gas.Year, gas.USA, 'b.-', label='United States')
plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='South Korea')
plt.plot(gas.Year, gas.Australia, 'y.-', label='Australia')
"""


plt.xticks(gas.Year[::3])

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()

plt.show()
