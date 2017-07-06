import pandas as pd

df = pd.DataFrame(
	{
		'A': [2, 3, 6, 8, 20, 27]
	}
)

df['B'] = df['A'].rolling(window=3).mean().shift(-2)

print (df)