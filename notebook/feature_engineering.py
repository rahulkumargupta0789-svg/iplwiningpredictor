import pandas as pd

# Load datasets
matches = pd.read_csv("../dataset/matches.csv")
deliveries = pd.read_csv("../dataset/deliveries.csv")

# First innings score
total_score = deliveries.groupby(['match_id', 'inning'])['total_runs'].sum().reset_index()
total_score = total_score[total_score['inning'] == 1]
total_score = total_score.rename(columns={'total_runs': 'first_innings_score'})

# Merge
matches = matches.merge(
    total_score[['match_id', 'first_innings_score']],
    left_on='id',
    right_on='match_id'
)

# Sirf second innings
match_df = matches[['id','city','winner','first_innings_score']]

second_innings = deliveries[deliveries['inning'] == 2]

# Merge second innings with match info
final_df = second_innings.merge(
    match_df,
    left_on='match_id',
    right_on='id'
)

print(final_df.head())
print("\nShape:", final_df.shape)