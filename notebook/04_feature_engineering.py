import pandas as pd

# Load datasets
matches = pd.read_csv("../dataset/matches.csv")
deliveries = pd.read_csv("../dataset/deliveries.csv")

# First innings score
total_score = deliveries.groupby(['match_id', 'inning'])['total_runs'].sum().reset_index()
total_score = total_score[total_score['inning'] == 1]
total_score.rename(columns={'total_runs':'first_innings_score'}, inplace=True)

# Merge with matches
matches = matches.merge(
    total_score[['match_id','first_innings_score']],
    left_on='id',
    right_on='match_id'
)

# Match info
match_df = matches[['id','city','winner','first_innings_score']]

# Second innings only
second_innings = deliveries[deliveries['inning'] == 2]

# Merge
final_df = second_innings.merge(
    match_df,
    left_on='match_id',
    right_on='id'
)

# Current score after every ball
final_df['current_score'] = final_df.groupby('match_id')['total_runs'].cumsum()

# Check output
print(final_df[['match_id','over','ball','total_runs','current_score']].head(20))