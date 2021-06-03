import requests
import pandas as pd
import matplotlib.pyplot as plt

url_fifa_data = 'https://raw.githubusercontent.com/KeithGalli/matplotlib_tutorial/master/fifa_data.csv'
res2 = requests.get(url_fifa_data, allow_redirects=True)

with open('fifa_data.csv', 'wb') as file:
    file.write(res2.content)

fifa = pd.read_csv('fifa_data.csv')


"""
Histograms
"""
# start

bins = [40, 50, 60, 70, 80, 90, 100]

plt.hist(fifa['Overall'], bins=bins, color='#abcdef')

plt.title('Distribution of Player Skills in FIFA')

plt.xticks(bins)

plt.xlabel('Skill level')
plt.ylabel('Number of players')

plt.show()
# end


"""
Pie chart
"""
# start

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

labels = ['Left', 'Right']
colors = ['#67bfb9', '#a869b3']

plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')

plt.title('Foot Preference of FIFA Players')

plt.show()
# end


"""
Boxes
"""
# start

plt.style.use('default')

plt.figure(figsize=(5, 8))

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']

MU = fifa.loc[fifa.Club == 'Manchester United']['Overall']

plt.title('Professional soccer team comparison')

labels = ['FC Barcelona', 'Real Madrid', 'Manchester United']
teams = [barcelona, madrid, MU]

plt.ylabel('FIFA Overall Rating')

boxes = plt.boxplot(
    teams, labels=labels, patch_artist=True, medianprops={
        'linewidth': 2, 'color': '#f5699c'
    }
)

for box in boxes['boxes']:
    box.set(color='#fcba03', linewidth=2)
    box.set(facecolor='#fce49d')

plt.show()

# end
