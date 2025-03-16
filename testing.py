import pandas as pd
df = pd.read_csv("test.txt", delim_whitespace=True)
print(df.head())
print(type(df['x']))