import pandas as pd

netflix = pd.read_csv('data/netflix_titles.csv')

print(netflix.dtypes)
print(netflix.iloc[0:10])
print(netflix.groupby('type').count())
print(netflix.groupby('director').count())
print(netflix.groupby('release_year').count())
