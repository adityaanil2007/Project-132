import pandas as pd

data = pd.read_csv("data.csv")

del data["Star_name"]

data = data.dropna()

data.to_csv("new_data.csv")










