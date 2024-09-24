import pandas as pd

# Load the training dataset
train_df = pd.read_parquet("/Users/adrianrich/Documents/python/chatbot_project/train-00000-of-00001.parquet")

# Print the column names to inspect them
print(train_df.columns)