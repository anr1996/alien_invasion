import pandas as pd

# Load the training dataset
train_df = pd.read_parquet("/Users/adrianrich/Documents/python/chatbot_project/train-00000-of-00001.parquet")

# Check the distribution of labels
label_counts = train_df['label'].value_counts()
print(label_counts)