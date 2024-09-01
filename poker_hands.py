import pandas as pd

# Helper function to convert to lowercase string
def convert_to_lower(answer):
    return answer.lower()

# Helper function to convert values to booleans:
def convert_to_boolean(answer):
    if answer == 'no':
        return False
    else:
        return True

# Function named load_hands
def load_hands(csv):
    # Create DataFrame
    df = pd.read_csv(csv)
    # Convert values to lowercase
    df['Won Round'] = df['Won Round'].apply(convert_to_lower)
    # Convert values "yes" and "no" to booleans:
    df['Won Round'] = df['Won Round'].apply(convert_to_boolean)
    # Handle missing values, replace NAN with "Unknown"
    # Handling the Player column
    df['Player'] = df['Player'].fillna('Unknown')
    # Handle other missing columns excluding the Player column
    df = df.dropna(subset=['Cards', 'Hand', 'Value Cards', 'Won Round'])
    # Split strings into lists in the Cards column
    df['Cards'] = df['Cards'].apply(lambda x: x.split(','))
    # The function returns the DataFrame
    return df

# Create DataFrame from the poker file
df = load_hands('poker_hands.csv')
# Display data
print(df.head())
print(df.info())

# Line printing the name of the player with the most wins in the table
# Booleans: 1 - True, 0 - False
# Sum all the 1's which indicates how many times the player won
# Then use idxmax to find the index with the highest number of wins
print(df.groupby('Player')['Won Round'].sum().idxmax())

# Write a condition if each player received a HIGH CARD
condition = df['Hand'] == 'high card'
# Use value_counts
# On the Value Cards column
# Then use idxmax which returns the index value with the highest count
# For the card value that occurred the most
print(df[condition]['Value Cards'].value_counts().idxmax())

# List the average wins per hand in the Hand column
# The set that gave the highest average wins
print(f"First Max: {df.groupby('Hand')['Won Round'].mean().idxmax()}")
# Find the second set with the highest average wins:
# Create a temporary parameter equal to the list of average wins per hand
temp_average_hands_win = df.groupby('Hand')['Won Round'].mean()
# Set the highest value with the highest average wins
max_win = df.groupby('Hand')['Won Round'].mean().max()
# Set a condition to display all sets except the set with the highest average wins found earlier
condition1 = temp_average_hands_win != max_win
# The second set with the most wins should be TWO PAIR
# Let's find the second one
print(f"Second Max: {temp_average_hands_win[condition1].idxmax()}")
