import pandas as pd

# Load the dataset
train_df = pd.read_parquet("/Users/adrianrich/Documents/python/chatbot_project/train-00000-of-00001.parquet")

# Example: Label as '1' if the utterances contain the word 'happy', else '0'
train_df['label'] = train_df['utterances'].apply(lambda x: 1 if 'happy' in x else 0)

# Save the updated DataFrame
train_df.to_parquet("/Users/adrianrich/Documents/python/chatbot_project/train_with_labels.parquet")

# Check the distribution of labels
label_counts = train_df['label'].value_counts()
print(label_counts)