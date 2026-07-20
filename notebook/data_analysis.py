import pandas as pd

# Load datasets
matches = pd.read_csv("../dataset/matches.csv")
deliveries = pd.read_csv("../dataset/deliveries.csv")

# Basic information
print("Matches Dataset")
print(matches.head())

print("\nDeliveries Dataset")
print(deliveries.head())

print("\nMatches Shape:", matches.shape)
print("Deliveries Shape:", deliveries.shape)

print("\nMissing Values in Matches")
print(matches.isnull().sum())

print("\nMissing Values in Deliveries")
print(deliveries.isnull().sum())