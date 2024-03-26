import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.table import Table
import numpy as np
from matplotlib.animation import FuncAnimation
import cv2
# Monopoly properties data
properties_data = [
    ['Go', 'None', '0'],
    ['Mediterranean Ave.', 'None', '0'],
    ['Community Chest', 'None', '0'],
    ['Baltic Ave.', 'None', '0'],
    ['Income Tax', 'None', '0'],
    ['Reading Railroad', 'None', '0'],
    ['Oriental Ave.', 'None', '0'],
    ['Chance', 'None', '0'],
    ['Vermont Ave.', 'None', '0'],
    ['Connecticut Ave.', 'None', '0'],
    ['Jail', 'None', '0'],
    ['St. Charles Place', 'None', '0'],
    ['Electric Company', 'None', '0'],
    ['States Ave.', 'None', '0'],
    ['Virginia Ave.', 'None', '0'],
    ['Pennsylvania Railroad', 'None', '0'],
    ['St. James Place', 'None', '0'],
    ['Community Chest', 'None', '0'],
    ['Tennessee Ave.', 'None', '0'],
    ['New York Ave.', 'None', '0'],
    ['Free Parking', 'None', '0'],
    ['Kentucky Ave.', 'None', '0'],
    ['Chance', 'None', '0'],
    ['Indiana Ave.', 'None', '0'],
    ['Illinois Ave.', 'None', '0'],
    ['B. & O. Railroad', 'None', '0'],
    ['Atlantic Ave.', 'None', '0'],
    ['Ventnor Ave.', 'None', '0'],
    ['Water Works', 'None', '0'],
    ['Marvin Gardens', 'None', '0'],
    ['Go to Jail', 'None', '0'],
    ['Pacific Ave.', 'None', '0'],
    ['North Carolina Ave.', 'None', '0'],
    ['Community Chest', 'None', '0'],
    ['Pennsylvania Ave.', 'None', '0'],
    ['Short Line', 'None', '0'],
    ['Chance', 'None', '0'],
    ['Park Place', 'None', '0'],
    ['Luxury Tax', 'None', '0'],
    ['Boardwalk', 'None', '0']
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

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 8))

def createFrame(players_data):
    # Create DataFrames
    df_properties = pd.DataFrame(properties_data)
    df_players = pd.DataFrame(players_data)

    # Create a table for properties
    table_properties = plt.table(cellText=properties_data, bbox=[0, 0, 0.6, 1], colLabels=('Property', 'Group', 'Color Code'), cellColours=property_table_colors, cellLoc='center')
    for i, col in enumerate(df_properties.columns):
        table_properties.auto_set_column_width([i])

    # Formatting for properties table
    table_properties.auto_set_font_size(False)
    table_properties.set_fontsize(8)
    table_properties.scale(1.2, 1.2)

    # Create a table for players
    table_players = plt.table(cellText=players_data, bbox=[0.65, 0.5, 0.35, 0.45], colLabels=('Player', 'Balance', 'Other'))
    for i, col in enumerate(df_players.columns):
        table_players.auto_set_column_width([i])
              
    # Create a "table" for next action
    table_ai_action = plt.text(0.65, 0.25, f'test', wrap=True, color='blue')

    plt.suptitle('Monopoly Properties and Players', fontsize=16)


# Create a function to generate each frame of the animation
def update(frame):
    # Generate your plot for each frame here
    plt.clf()
    createFrame(np.random.rand(2,3))

# # Create a figure and axis object
# fig, ax = plt.subplots()

# Create an animation object
ani = FuncAnimation(fig, update, frames=range(10), repeat=False)

# Save each frame as a PNG image
length = 20
for i in range(length):
    update(i)  # Generate the plot for each frame
    plt.savefig(f'frame_{i:03d}.png')

# Convert PNG images to an MP4 video using OpenCV
frames = []
for i in range(length):
    img = cv2.imread(f'frame_{i:03d}.png')
    height, width, layers = img.shape
    size = (width,height)
    frames.append(img)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 1.0, size)

# Write the frames to the video
for frame in frames:
    out.write(frame)

# Release the VideoWriter object
out.release()

# Cleanup: Remove the PNG images
import os
for i in range(length):
    os.remove(f'frame_{i:03d}.png')
