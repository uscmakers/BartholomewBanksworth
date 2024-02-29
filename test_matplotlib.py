import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.table import Table

# Monopoly properties data
properties_data = {
    'Property': ['Go', 'Mediterranean Ave.', 'Community Chest', 'Baltic Ave.', 'Income Tax',
                 'Reading Railroad', 'Oriental Ave.', 'Chance', 'Vermont Ave.', 'Connecticut Ave.',
                 'Jail', 'St. Charles Place', 'Electric Company', 'States Ave.', 'Virginia Ave.',
                 'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Ave.', 'New York Ave.',
                 'Free Parking', 'Kentucky Ave.', 'Chance', 'Indiana Ave.', 'Illinois Ave.',
                 'B. & O. Railroad', 'Atlantic Ave.', 'Ventnor Ave.', 'Water Works', 'Marvin Gardens',
                 'Go to Jail', 'Pacific Ave.', 'North Carolina Ave.', 'Community Chest', 'Pennsylvania Ave.', 'Short Line',
                 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk'],
    'Color': ['None', 'Brown', 'None', 'Brown', 'None',
              'Railroad', 'Light Blue', 'None', 'Light Blue', 'Light Blue',
              'None', 'Pink', 'Utility', 'Pink', 'Pink',
              'Railroad', 'Orange', 'None', 'Orange', 'Orange',
              'None', 'Red', 'None', 'Red', 'Red',
              'Railroad', 'Yellow', 'Yellow', 'Utility', 'Yellow',
              'None', 'Green', 'Green', 'None', 'Green', 'Railroad',
              'None', 'Dark Blue', 'None', 'Dark Blue'],
    'Group': ['Special', 'Low Rent', 'Special', 'Low Rent', 'Special',
              'Railroad', 'Medium Rent', 'Special', 'Medium Rent', 'Medium Rent',
              'Special', 'High Rent', 'Special', 'High Rent', 'High Rent',
              'Railroad', 'Medium Rent', 'Special', 'Medium Rent', 'Medium Rent',
              'Special', 'High Rent', 'Special', 'High Rent', 'High Rent',
              'Railroad', 'Medium Rent', 'Medium Rent', 'Special', 'Medium Rent',
              'Special', 'Medium Rent', 'Medium Rent', 'Special', 'Medium Rent', 'Railroad',
              'Special', 'High Rent', 'Special', 'High Rent'],
    'Color Code': ['white', '#8B4513', 'white', '#8B4513', 'white',
                   '#A9A9A9', '#ADD8E6', 'white', '#ADD8E6', '#ADD8E6',
                   'white', '#FFC0CB', 'white', '#FFC0CB', '#FFC0CB',
                   '#A9A9A9', '#FFA500', 'white', '#FFA500', '#FFA500',
                   'white', '#FF0000', 'white', '#FF0000', '#FF0000',
                   '#A9A9A9', '#FFFF00', '#FFFF00', 'white', '#FFFF00',
                   'white', '#008000', '#008000', 'white', '#008000', '#A9A9A9',
                   'white', '#000080', 'white', '#000080']
}

# Player data
players_data = {
    'Player': ['Player 1', 'Player 2', 'Player 3'],
    'Position': [0, 10, 20],
    'Balance': [1500, 1500, 1500],
    'Owned Properties': ['', '', '']
}

# Create DataFrames
df_properties = pd.DataFrame(properties_data)
df_players = pd.DataFrame(players_data)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

# Create a table for properties
table_properties = Table(ax, bbox=[0, 0, 0.6, 1])
for i, col in enumerate(df_properties.columns):
    table_properties.auto_set_column_width([i])
    for j, value in enumerate(df_properties[col]):
        cell_color = df_properties.at[j, 'Color Code'] if col == 'Color' else 'white'
        table_properties.add_cell(j, i, width=1, height=1, text=value, loc='center', facecolor=cell_color)

# Add headers and title for properties table
table_properties.auto_set_font_size(False)
table_properties.set_fontsize(10)
table_properties.scale(1.2, 1.2)
table_properties.add_cell(0, 0, width=1, height=1, text='Property', loc='center', facecolor='lightgray')
table_properties.add_cell(0, 1, width=1, height=1, text='Color', loc='center', facecolor='lightgray')
table_properties.add_cell(0, 2, width=1, height=1, text='Group', loc='center', facecolor='lightgray')

# Create a table for players
table_players = Table(ax, bbox=[0.65, 0.1, 0.35, 0.8])
for i, col in enumerate(df_players.columns):
    table_players.auto_set_column_width([i])
    for j, value in enumerate(df_players[col]):
        table_players.add_cell(j, i, width=1, height=1, text=value, loc='center', facecolor='lightgray')

# Add headers and title for players table
table_players.auto_set_font_size(False)
table_players.set_fontsize(12)
table_players.scale(1.2, 1.2)
table_players.add_cell(0, 0, width=1, height=1, text='Player', loc='center', facecolor='lightgray')
table_players.add_cell(0, 1, width=1, height=1, text='Position', loc='center', facecolor='lightgray')
table_players.add_cell(0, 2, width=1, height=1, text='Balance', loc='center', facecolor='lightgray')
table_players.add_cell(0, 3, width=1, height=1, text='Owned Properties', loc='center', facecolor='lightgray')

# Add tables to the axis
ax.add_table(table_properties)
ax.add_table(table_players)

plt.suptitle('Monopoly Properties and Players', fontsize=16)
plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.table import Table
# import numpy as np
# import time

# # Dummy function to update game state
# def update_game_state():
#     # Generate random changes in player state
#     df_players['Position'] = np.random.randint(0, len(df_properties), size=len(df_players))
#     df_players['Balance'] += np.random.randint(-100, 100, size=len(df_players))
#     df_players['Owned Properties'] = np.random.choice(df_properties['Property'], size=len(df_players), replace=False)

# # Dummy data initialization
# np.random.seed(42)
# update_game_state()

# # Create a figure and axis
# fig, ax = plt.subplots(figsize=(12, 8))
# ax.axis('off')

# # Create a table for properties
# table_properties = Table(ax, bbox=[0, 0, 0.6, 1])
# for i, col in enumerate(df_properties.columns):
#     table_properties.auto_set_column_width([i])
#     for j, value in enumerate(df_properties[col]):
#         cell_color = df_properties.at[j, 'Color Code'] if col == 'Color' else 'white'
#         table_properties.add_cell(j, i, width=1, height=1, text=value, loc='center', facecolor=cell_color)

# # Add headers and title for properties table
# table_properties.auto_set_font_size(False)
# table_properties.set_fontsize(10)
# table_properties.scale(1.2, 1.2)
# table_properties.add_cell(0, 0, width=1, height=1, text='Property', loc='center', facecolor='lightgray')
# table_properties.add_cell(0, 1, width=1, height=1, text='Color', loc='center', facecolor='lightgray')
# table_properties.add_cell(0, 2, width=1, height=1, text='Group', loc='center', facecolor='lightgray')

# # Create a table for players
# table_players = Table(ax, bbox=[0.65, 0.1, 0.35, 0.8])
# for i, col in enumerate(df_players.columns):
#     table_players.auto_set_column_width([i])
#     for j, value in enumerate(df_players[col]):
#         table_players.add_cell(j, i, width=1, height=1, text=value, loc='center', facecolor='lightgray')

# # Add headers and title for players table
# table_players.auto_set_font_size(False)
# table_players.set_fontsize(12)
# table_players.scale(1.2, 1.2)
# table_players.add_cell(0, 0, width=1, height=1, text='Player', loc='center', facecolor='lightgray')
# table_players.add_cell(0, 1, width=1, height=1, text='Position', loc='center', facecolor='lightgray')
# table_players.add_cell(0, 2, width=1, height=1, text='Balance', loc='center', facecolor='lightgray')
# table_players.add_cell(0, 3, width=1, height=1, text='Owned Properties', loc='center', facecolor='lightgray')

# # Add tables to the axis
# ax.add_table(table_properties)
# ax.add_table(table_players)

# plt.suptitle('Monopoly Properties and Players', fontsize=16)
# plt.show()

# # Function to update the plot dynamically
# def update_plot():
#     update_game_state()

#     # Update data in tables
#     table_properties.auto_set_column_width([i for i in range(len(df_properties.columns))])
#     for i, col in enumerate(df_properties.columns):
#         for j, value in enumerate(df_properties[col]):
#             cell_color = df_properties.at[j, 'Color Code'] if col == 'Color' else 'white'
#             table_properties[(j + 1, i)].set_text(value)
#             table_properties[(j + 1, i)].set_facecolor(cell_color)

#     table_players.auto_set_column_width([i for i in range(len(df_players.columns))])
#     for i, col in enumerate(df_players.columns):
#         for j, value in enumerate(df_players[col]):
#             table_players[(j + 1, i)].set_text(value)

#     # Redraw the plot
#     plt.draw()
#     plt.pause(1)  # Add a short pause to make changes visible

# # Example of updating the plot dynamically
# for _ in range(5):
#     update_plot()
#     time.sleep(1)  # Simulating some game progress

# plt.show()
