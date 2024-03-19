import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.table import Table

# Monopoly properties data
properties_data = [
    ['Go', 'Special', 'white'],
    ['Mediterranean Ave.', 'Low Rent', '#8B4513'],
    ['Community Chest', 'Special', 'white'],
    ['Baltic Ave.', 'Low Rent', '#8B4513'],
    ['Income Tax', 'Special', 'white'],
    ['Reading Railroad', 'Railroad', '#A9A9A9'],
    ['Oriental Ave.', 'Medium Rent', '#ADD8E6'],
    ['Chance', 'Special', 'white'],
    ['Vermont Ave.', 'Medium Rent', '#ADD8E6'],
    ['Connecticut Ave.', 'Medium Rent', '#ADD8E6'],
    ['Jail', 'Special', 'white'],
    ['St. Charles Place', 'High Rent', '#FFC0CB'],
    ['Electric Company', 'Special', 'white'],
    ['States Ave.', 'High Rent', '#FFC0CB'],
    ['Virginia Ave.', 'High Rent', '#FFC0CB'],
    ['Pennsylvania Railroad', 'Railroad', '#A9A9A9'],
    ['St. James Place', 'Medium Rent', '#FFA500'],
    ['Community Chest', 'Special', 'white'],
    ['Tennessee Ave.', 'Medium Rent', '#FFA500'],
    ['New York Ave.', 'Medium Rent', '#FFA500'],
    ['Free Parking', 'Special', 'white'],
    ['Kentucky Ave.', 'High Rent', '#FF0000'],
    ['Chance', 'Special', 'white'],
    ['Indiana Ave.', 'High Rent', '#FF0000'],
    ['Illinois Ave.', 'High Rent', '#FF0000'],
    ['B. & O. Railroad', 'Medium Rent', '#A9A9A9'],
    ['Atlantic Ave.', 'Medium Rent', '#FFFF00'],
    ['Ventnor Ave.', 'Medium Rent', '#FFFF00'],
    ['Water Works', 'Special', 'white'],
    ['Marvin Gardens', 'Medium Rent', '#FFFF00'],
    ['Go to Jail', 'Special', 'white'],
    ['Pacific Ave.', 'Medium Rent', '#008000'],
    ['North Carolina Ave.', 'Medium Rent', '#008000'],
    ['Community Chest', 'Special', 'white'],
    ['Pennsylvania Ave.', 'High Rent', '#000080'],
    ['Short Line', 'Medium Rent', '#A9A9A9'],
    ['Chance', 'Special', 'white'],
    ['Park Place', 'High Rent', '#000080'],
    ['Luxury Tax', 'Special', 'white'],
    ['Boardwalk', 'High Rent', '#000080']
]

property_table_colors = [['None', 'None', 'None'], 
                         ['indianred', 'None', 'None'], 
                         ['None', 'None', 'None'],
                         ['indianred', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Silver', 'None', 'None'],
                         ['Aqua', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Aqua', 'None', 'None'],
                         ['Aqua', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['mediumpurple', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['mediumpurple', 'None', 'None'],
                         ['mediumpurple', 'None', 'None'],
                         ['Silver', 'None', 'None'],
                         ['Orange', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Orange', 'None', 'None'],
                         ['Orange', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Red', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Red', 'None', 'None'],
                         ['Red', 'None', 'None'],
                         ['Silver', 'None', 'None'],
                         ['Yellow', 'None', 'None'],
                         ['Yellow', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Yellow', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['springgreen', 'None', 'None'],
                         ['springgreen', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['springgreen', 'None', 'None'],
                         ['Silver', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['cornflowerblue', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['cornflowerblue', 'None', 'None']]

# Player data
players_data = [
    [0, 1500, ''],
    [10, 1500, '']
]

# Create DataFrames
df_properties = pd.DataFrame(properties_data)
df_players = pd.DataFrame(players_data)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 8))
ax.axis('off')

# Create a table for properties
table_properties = plt.table(cellText=properties_data, bbox=[0, 0, 0.6, 1], colLabels=('Property', 'Group', 'Color Code'), cellColours=property_table_colors)
for i, col in enumerate(df_properties.columns):
    table_properties.auto_set_column_width([i])

# Formatting for properties table
table_properties.auto_set_font_size(False)
table_properties.set_fontsize(10)
table_properties.scale(1.2, 1.2)

# # Create a table for players
# table_players = plt.table(cellText=playersata, bbox=[0.65, 0.1, 0.35, 0.8], colLabels=('Player', 'Balance', 'Other'))
# for i, col in enumerate(df_players.columns):
#     table_players.auto_set_column_width([i])

# # Formatting for players table
# table_players.auto_set_font_size(False)
# table_players.set_fontsize(12)
# table_players.scale(1.2, 1.2)

# Add tables to the axis
ax.add_table(table_properties)
# ax.add_table(table_players)

plt.suptitle('Monopoly Properties and Players', fontsize=16)
plt.show()