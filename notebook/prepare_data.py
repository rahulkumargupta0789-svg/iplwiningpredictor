import pandas as pd

# Load datasets
matches = pd.read_csv("../dataset/matches.csv")
deliveries = pd.read_csv("../dataset/deliveries.csv")

# Total score of first innings
total_score = deliveries.groupby(['match_id', 'inning'])['total_runs'].sum().reset_index()

# Sirf first innings ka score
total_score = total_score[total_score['inning'] == 1]

# Rename column
total_score = total_score.rename(columns={'total_runs': 'first_innings_score'})

print(total_score.head())

print("\nShape:", total_score.shape)