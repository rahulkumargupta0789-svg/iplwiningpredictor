import pandas as pd

# Load datasets
matches = pd.read_csv("../dataset/matches.csv")
deliveries = pd.read_csv("../dataset/deliveries.csv")

# First innings score
total_score = deliveries.groupby(['match_id','inning'])['total_runs'].sum().reset_index()
total_score = total_score[total_score['inning'] == 1]
total_score.rename(columns={'total_runs':'first_innings_score'}, inplace=True)

# Merge
matches = matches.merge(
    total_score[['match_id','first_innings_score']],
    left_on='id',
    right_on='match_id'
)

match_df = matches[['id','city','winner','first_innings_score']]

# Second innings
second_innings = deliveries[deliveries['inning'] == 2]

final_df = second_innings.merge(
    match_df,
    left_on='match_id',
    right_on='id'
)

# Current Score
final_df['current_score'] = final_df.groupby('match_id')['total_runs'].cumsum()

# Target
final_df['target'] = final_df['first_innings_score'] + 1

# Runs Left
final_df['runs_left'] = final_df['target'] - final_df['current_score']

# Balls Faced
final_df['balls_bowled'] = (final_df['over'] - 1) * 6 + final_df['ball']

# Balls Left
final_df['balls_left'] = 120 - final_df['balls_bowled']

# Wickets Fallen
final_df['player_dismissed'] = final_df['player_dismissed'].fillna(0)
final_df['wicket'] = final_df['player_dismissed'].apply(lambda x: 0 if x == 0 else 1)
final_df['wickets_left'] = 10 - final_df.groupby('match_id')['wicket'].cumsum()

# Output
print(final_df[[
    'match_id',
    'current_score',
    'target',
    'runs_left',
    'balls_left',
    'wickets_left'
]].head(20))